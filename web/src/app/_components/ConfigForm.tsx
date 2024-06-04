const configProperties = ['inp1', 'inp2', 'inp3', 'inp4', 'inp5', 'inp6', 'inp7', 'inp8']

export default function ConfigForm() {
    return (
        <div className="px-4">
            <form className="bg-white w-full lg:overflow-scroll p-4">
                <div className="grid lg:grid-cols-10 grid-cols-5 w-full items-center lg:gap-x-16 gap-x-4 gap-y-4">
                    {configProperties.map((property) => (
                        <>
                            <div className="flex col-span-2 md:col-span-1 justify-self-start h-8"><span className="flex items-center">Inp1:</span></div>
                            <input type="text" className="border rounded-lg bg-gray-100 h-8 col-span-3 md:col-span-4" id="inp1"></input>
                        </>
                    ))}
                </div>
                <div className="flex justify-center lg:pt-8 pt-4 pb-4">
                    <button className="bg-blue-400 border rounded-lg w-24 h-8"><span className="text-white">Kekw</span></button>
                </div>
            </form>
        </div>
    )
}