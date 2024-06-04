export default function Header({title}: {title: string}) {
    return (
      <div className="pb-4">
        <div className="flex justify-between p-4 border-b bg-white items-center">
          <h2 className="px-2 font-semibold">{title}</h2>
          <h2 className="px-2">Welcome back, User</h2>
        </div>
      </div>
    );
  } 