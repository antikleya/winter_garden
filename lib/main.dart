import 'dart:async';
import 'package:flutter/material.dart';
import 'package:syncfusion_flutter_charts/charts.dart';
import 'package:firebase_core/firebase_core.dart';
import 'firebase_options.dart';
import 'package:firebase_database/firebase_database.dart';
import 'package:intl/intl.dart';
import 'models/ChartData.dart';
import 'telegram_client.dart';
import 'telegram_config.dart';
import 'alertHandler.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );

  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Winter Garden Dashboard',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // Try running your application with "flutter run". You'll see the
        // application has a blue toolbar. Then, without quitting the app, try
        // changing the primarySwatch below to Colors.green and then invoke
        // "hot reload" (press "r" in the console where  you ran "flutter run",
        // or simply save your changes to "hot reload" in a Flutter IDE).
        // Notice that the counter didn't reset back to zero; the application
        // is not restarted.
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  late TooltipBehavior _tooltipBehavior;
  final _database = FirebaseDatabase.instance.ref();
  late ZoomPanBehavior _zoomPanBehavior;
  late TelegramClient _telegramClient;
  late ChartData _lastDataPoint;
  late Timer timer;
  late AlertHandler alertHandler;

  @override
  void initState(){
    _telegramClient =  TelegramClient(
      chatId: telegramConfig['chatId']!,
      botToken: telegramConfig['botToken']!,
    );
    _zoomPanBehavior = ZoomPanBehavior(
        enablePinching: true,
        enableMouseWheelZooming: true,
        enableSelectionZooming: true,
        enablePanning: true,
        zoomMode: ZoomMode.x);
    _tooltipBehavior = TooltipBehavior(enable: true,
      duration: 10000,
      format: 'Время -> point.x\nseries.name -> point.y');
    alertHandler = AlertHandler(
        telegramClient: _telegramClient,
        timeInterval: 40);
    Timer.periodic(const Duration(seconds: 30), (timer) {
      alertHandler.handleAlert(_lastDataPoint.timestamp);
    });
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
      padding: const EdgeInsets.all(10),
      child: Center(
          child: StreamBuilder<DatabaseEvent>(
        builder: (context, snapshot) {
          if (snapshot.hasError ||
              snapshot.connectionState == ConnectionState.waiting) {
            return const CircularProgressIndicator();
          } else {
            var dataSource = <ChartData>[];
            var data = snapshot.data!.snapshot.children;
            for (final child in data) {
              var returnable = child.value as Map<String, dynamic>;
              dataSource.add(ChartData.fromRTDB(returnable));
            }
            _lastDataPoint = dataSource.last;
            return SfCartesianChart(
                title: ChartTitle(text: 'Temperature graph'),
                // Enable legend
                legend: Legend(isVisible: true),
                // Enable tooltip
                tooltipBehavior: _tooltipBehavior,
                zoomPanBehavior: _zoomPanBehavior,
                series: <ChartSeries>[
                  FastLineSeries<ChartData, DateTime>(
                    dataSource: dataSource,
                    xValueMapper: (ChartData data, _) => data.timestamp,
                    yValueMapper: (ChartData data, _) => data.temperature,
                    color: Colors.blue,
                    name: 'Температура',
                  ),
                  LineSeries<ChartData, DateTime>(
                    dataSource: dataSource,
                    xValueMapper: (ChartData data, _) => data.timestamp,
                    yValueMapper: (ChartData data, _) => data.speed,
                    pointColorMapper: (ChartData data, _) =>
                      data.speed < 5 ? Colors.teal : Colors.red,
                    name: 'Обороты пушки',
                  ),
                  FastLineSeries<ChartData, DateTime>(
                    dataSource: dataSource,
                    xValueMapper: (ChartData data, _) => data.timestamp,
                    yValueMapper: (ChartData data, _) => data.humidity,
                    color: Colors.green,
                    name: 'Влажность',
                  ),
                  FastLineSeries<ChartData, DateTime>(
                    dataSource: dataSource,
                    xValueMapper: (ChartData data, _) => data.timestamp,
                    yValueMapper: (ChartData data, _) =>
                      data.humidifierRelayState ? 15 : 10,
                    color: Colors.deepOrange,
                    name: 'Испаритель',
                  ),
                ],
                primaryXAxis: DateTimeAxis(
                  edgeLabelPlacement: EdgeLabelPlacement.shift,
                  dateFormat: DateFormat("M/d H:mm"),
                  intervalType: DateTimeIntervalType.minutes
                ),
            );
          }
        },
        stream: _database.child("Log").onValue,
      )),
    ));

  }
}
