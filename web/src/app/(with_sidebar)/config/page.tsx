import Header from "../../_components/Header"
import ConfigForm from "../../_components/ConfigForm"

export default function Config() {
    return (
        <div className="bg-gray-100 min-h-screen w-full">
            <Header title="Config editor"/>
            <ConfigForm />
        </div>
    )
}