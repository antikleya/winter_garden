import 'telegram_client.dart';


class AlertHandler {
  AlertHandler({
    required this.telegramClient,
    this.timeInterval = 40,
});
  final TelegramClient telegramClient;
  int timeInterval;
  static bool alertState = false;

  void handleAlert(DateTime date){
    int difference = DateTime.now().difference(date).inMinutes;
    if (difference > timeInterval) {
      if (!alertState) {
        telegramClient.sendMessage("\u2757\u2757\u2757ALERT\u2757\u2757\u2757: No data for $difference minutes");
        alertState = true;
      }
    }
    else {alertState = false;}
  }

  void setTimeInterval(int timeInterval){ this.timeInterval = timeInterval; }
}