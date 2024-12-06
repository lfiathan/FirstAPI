
import React, { useEffect, useState } from "react";
import API from "../api";
import './KaryawanList.css';

const KaryawanList = () => {
  const [karyawan, setKaryawan] = useState([]);

  useEffect(() => {
    API.get("/karyawan/")
      .then((response) => {
        setKaryawan(response.data);
      })
      .catch((error) => {
        console.error("Failed to fetch karyawan:", error);
      });
  }, []);

  return (
    <div>
      <h2>Karyawan List</h2>
      <ul>
        {karyawan.map((item) => (
          <li key={item.id}>
            {item.nama_lengkap} - {item.email}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default KaryawanList;
