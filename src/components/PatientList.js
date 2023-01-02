import React, { useEffect, useState } from 'react'
import { getpatient, addpatient, editpatient , deletepatient} from '../services/ApiService'
import AddPatient from './AddPatient'
import EditPatient from './EditPatient'

export default function PatientList() {

const [patients, setPatients] = useState([])
const [showAddPatientForm, setShowAddPatientForm] = useState(false)
const [showEditPatientForm, setShowEditPatientForm] = useState(false)
const [selectedEditData, setSelectedEditData] = useState()

useEffect(() => {
    let mount = true
    getpatient()
    .then(res => {console.log("res from api", res)
        setPatients(res)
        return() => mount = false
    })
}, [])

const handleAddSubmit = (e) => {
    addpatient(e.target)
    .then(res => {
        setPatients(res)
    })
}

const handleEditBtn = (patient) => {
    setSelectedEditData(patient)
    console.log("patient selected is", patient)
    setShowEditPatientForm(true)
    setShowAddPatientForm(false)
}

const handleEditSubmit = (e, id) => {
    editpatient(id, e.target)
    .then(res => {
        setPatients(res)
    })
}
function handleCancelBtn() {
    setShowAddPatientForm(false)
}
const handleDeleteBtn = (id) => {
    deletepatient(id)
    .then(res => {
        setPatients(patients.filter(p=> p.patient_id !== id))
    })
}

  return (
    <>
    <h3>PATIENT LIST</h3>
    <table border={"2px"} cellPadding={"10px"}>
        <thead>
            <tr>
                <td>First Name</td>
                <td>Last Name</td>
                <td>Blood Group</td>
                <td>Action</td>
            </tr>
        </thead>
        <tbody>
            {patients.map(patient => {
                return <tr key={patient.patient_id}>
                <td>{patient.first_name}</td>
                <td>{patient.last_name}</td>
                <td>{patient.blood}</td>
                <td><button onClick={()=>handleEditBtn(patient)}>Edit</button> <button onClick={()=>handleDeleteBtn(patient.patient_id)}>Delete</button></td>
            </tr>
            })}
            
        </tbody>
    </table>
    <button onClick={()=>setShowAddPatientForm(true)}>Add New Patient</button>
    {showAddPatientForm && <AddPatient handleAddSubmit={handleAddSubmit} handleCancelBtn = {handleCancelBtn}/>}
    {showEditPatientForm && <EditPatient handleEditSubmit={handleEditSubmit} selectedEditData = {selectedEditData}/>}
    </>
  )
}
