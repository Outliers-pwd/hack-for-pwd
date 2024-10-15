import { Routes, Route, Navigate } from "react-router-dom"
import Home from './pages/Home'
import Register from "./pages/Register"
import Login from "./pages/Login"
import NotFound from "./pages/NotFound"
import { ProtectedRoute } from "./components/ProtectedRoute"
export default function App(){
  function Logout(){
    localStorage.clear()
    return <Navigate to='/login/'/>
  }

  function RegisterAndLogout(){
    localStorage.clear()
    return <Register/>
  }

  return (
    <>
    <Routes>
      <Route path="/" element={
        <ProtectedRoute>
          <Home/>
        </ProtectedRoute>
      }/>

      <Route path="login/" element={<Login/>} />
      <Route path="register/" element={<RegisterAndLogout/>} />
      <Route path="logout/" element={<Logout/>} />
      <Route path="*" element={<NotFound/>}/>
    </Routes>
    </>
  )
}