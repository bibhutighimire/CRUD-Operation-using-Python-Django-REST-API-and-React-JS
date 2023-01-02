import axios from "axios";

export  function getpatient() {
  return axios.get('http://127.0.0.1:8000/patient/')
  .then(res => {
    return res.data
  })}

export  function addpatient(patient) {
return axios.post('http://127.0.0.1:8000/patient/',
{
    patient_id: null,
    first_name: patient.first_name.value,
    last_name: patient.last_name.value,
    blood: patient.blood.value,
})
.then(res => {
    return res.data
})}

export  function editpatient(id, patient) {
    return axios.put('http://127.0.0.1:8000/patient/'+id+'/',
    {
        first_name: patient.first_name.value,
        last_name: patient.last_name.value,
        blood: patient.blood.value,
    })
    .then(res => {
        return res.data
    })}

export  function deletepatient(id) {
    return axios.delete('http://127.0.0.1:8000/patient/'+id+'/')
    .then(res => {
        return res.data
    })}