import React from "react";
import KaryawanList from "./components/KaryawanList";
import KaryawanForm from "./components/KaryawanForm";

const App = () => {
  return (
    <div>
      <h1>MyApp Frontend</h1>
      <KaryawanForm />
      <KaryawanList />
    </div>
  );
};

export default App;

