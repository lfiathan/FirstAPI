
import React, { useState } from "react";
import API from "../api";
import './KaryawanForm.css';

const KaryawanForm = () => {
  const [formData, setFormData] = useState({
    nama_lengkap: "",
    email: "",
    nomor_telepon: "",
    tanggal_lahir: "",
    alamat: "",
    tanggal_masuk: "",
    departemen: null,
    jabatan: null,
    status: "aktif",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    API.post("/karyawan/", formData)
      .then((response) => {
        alert("Karyawan added successfully!");
        setFormData({
          nama_lengkap: "",
          email: "",
          nomor_telepon: "",
          tanggal_lahir: "",
          alamat: "",
          tanggal_masuk: "",
          departemen: null,
          jabatan: null,
          status: "aktif",
        });
      })
      .catch((error) => {
        console.error("Error adding karyawan:", error);
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Add Karyawan</h2>
      <input
        type="text"
        name="nama_lengkap"
        placeholder="Nama Lengkap"
        value={formData.nama_lengkap}
        onChange={handleChange}
      />
      <input
        type="email"
        name="email"
        placeholder="Email"
        value={formData.email}
        onChange={handleChange}
      />
      <input
        type="text"
        name="nomor_telepon"
        placeholder="Nomor Telepon"
        value={formData.nomor_telepon}
        onChange={handleChange}
      />
      <input
        type="date"
        name="tanggal_lahir"
        value={formData.tanggal_lahir}
        onChange={handleChange}
      />
      <textarea
        name="alamat"
        placeholder="Alamat"
        value={formData.alamat}
        onChange={handleChange}
      ></textarea>
      <input
        type="date"
        name="tanggal_masuk"
        value={formData.tanggal_masuk}
        onChange={handleChange}
      />
      <select name="status" value={formData.status} onChange={handleChange}>
        <option value="aktif">Aktif</option>
        <option value="nonaktif">Nonaktif</option>
      </select>
      <button type="submit">Submit</button>
    </form>
  );
};

export default KaryawanForm;
