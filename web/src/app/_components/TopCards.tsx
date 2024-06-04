import { IoIosCheckmarkCircle } from "react-icons/io";


export default function TopCards() {
    return (
        <div className="grid lg:grid-cols-4 gap-4 p-4">
            <div className="col-span-1 bg-white flex justify-between w-full border p-4 rounded-lg">
                <div className="flex flex-col w-full pb-2">
                    <span className="text-2xl font-bold text-red-600"> 20с</span>
                    <p className="text-gray-700 text-sm pt-1">
                        Средняя температура сегодня
                    </p>
                </div>
                <p className="bg-green-200 flex justify-center items-center p2 rounded-lg w-16">
                    <span className="p-2">
                        <IoIosCheckmarkCircle size={32} />
                    </span>
                </p>
            </div>
            <div className="col-span-1 bg-white flex justify-between w-full border p-4 rounded-lg">
                <div className="flex flex-col w-full pb-2">
                    <span className="text-2xl font-bold text-red-600"> 20с</span>
                    <p className="text-gray-700 text-sm pt-1">
                        Максимальная температура сегодня
                    </p>
                </div>
                <p className="bg-green-200 flex justify-center items-center p2 rounded-lg w-16">
                    <span className="p-2">
                        <IoIosCheckmarkCircle size={32} />
                    </span>
                </p>
            </div>
            <div className="bg-white flex justify-between w-full border p-4 rounded-lg">
                <div className="flex flex-col w-full pb-2">
                    <span className="text-2xl font-bold text-blue-600"> 20%</span>
                    <p className="text-gray-700 text-sm pt-1">
                        Максимальная влажность сегодня
                    </p>
                </div>
                <p className="bg-green-200 flex justify-center items-center p2 rounded-lg w-16">
                    <span className="p-2">
                        <IoIosCheckmarkCircle size={32} />
                    </span>
                </p>
            </div>
            <div className="bg-white flex justify-between w-full border p-4 rounded-lg">
                <div className="flex flex-col w-full pb-2">
                    <span className="text-2xl font-bold text-blue-600"> 20%</span>
                    <p className="text-gray-700 text-sm pt-1">
                        Средняя влажность сегодня
                    </p>
                </div>
                <p className="bg-green-200 flex justify-center items-center p2 rounded-lg w-16">
                    <span className="p-2">
                        <IoIosCheckmarkCircle size={32} />
                    </span>
                </p>
            </div>
        </div>
    )
}