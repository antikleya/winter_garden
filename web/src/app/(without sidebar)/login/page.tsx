import LoginForm from "@/app/_components/LoginForm";
import RegistrationForm from "@/app/_components/RegistrationForm";


export default function LoginPage() {
    return (
        <div className="w-full flex justify-center pt-6">
            <div className="grid lg:grid-cols-5 content-center min-h-[90vh] w-2/3 gap-8">
            <div className="grid grid-cols-1 lg:col-span-2 content-center pt-16 lg:pt-0">
                <div className="flex items-center justify-center text-xl">Войти</div>
                <LoginForm />
            </div>
            <div className="w-full col-span-1 h-full lg:px-12 flex lg:justify-center ">
                <div className="h-full w-0 border hidden lg:block"></div>
                <div className="h-0 w-full border block lg:hidden"></div>
            </div>
            <div className="grid grid-cols-1 lg:col-span-2 content-center pt-16 lg:pt-0">
                <div className="flex items-center justify-center text-xl">Зарегистрироваться</div>
                <RegistrationForm />
            </div>
        </div>
        </div>
    )
}