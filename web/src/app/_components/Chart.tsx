"use client"

import { 
    Chart as ChartJS, 
    TimeScale, 
    Tooltip, 
    Legend,
    Title,
    LineElement,
    LinearScale,
    PointElement,
    CategoryScale
} from 'chart.js'
import { useEffect, useRef, useState } from 'react';
import {ru} from 'date-fns/locale'
import 'chartjs-adapter-date-fns';
import { Line } from 'react-chartjs-2';
import { ChartData } from 'chart.js';

ChartJS.register(
    TimeScale,
    LinearScale,
    LineElement,
    PointElement,
    Tooltip,
    Legend,
    Title
)

const options = {
    scales: {
        x: {
            type: 'time' as const
        },
    },
    adapters: {
        date: {
            locale: ru
        }
    },
    plugins: {
        legend: {
            position: 'top' as const,
        },
        title: {
            display: true,
            text: 'Test Chart'
        }
    },
    maintainAspectRatio: false,
    responsive: true
}


export default function Chart() {
    const [chartData, setChartData] = useState<ChartData<'line', number[], string>>({
        datasets: [],
    });

    useEffect(() => {
        setChartData({
            labels: ['2022-12-05', '2022-12-06', '2022-12-07'],
            datasets: [
                {
                    label: 'test',
                    data: [1, 2, 3],
                    borderColor: 'rgb(53, 162, 235)',
                    backgroundColor: 'rgb(53, 162, 235, 0.4)'
                }
            ]
        });
    }, [])

    return (
        <div className='p-4 grid grid-cols-1 gap-4'>
            <div className="w-full relative lg:h-[70vh] h-[50vh] m-auto p-4 border rounded-lg bg-white">
                <Line 
                    data={chartData}
                    options={options}
                />
            </div>
        </div>
    );
}