import Header from "../_components/Header";
import TopCards from "../_components/TopCards";
import Chart from "../_components/Chart";

export default function Home() {
  return (
    <div className="bg-gray-100 min-h-screen w-full">
      <Header title="Danshboard" />
      <TopCards />
      <Chart />
    </div>
  );
}
