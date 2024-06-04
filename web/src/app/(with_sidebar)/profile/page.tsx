import Profile from "../../_components/Profile"
import Header from "../../_components/Header"

export default function ProfilePage() {
    return (
        <div className="bg-gray-100 min-h-screen w-full">
            <Header title="Profile editor"/>
            <Profile />
        </div>
    )
}