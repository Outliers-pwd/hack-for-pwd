import { useState } from 'react'
import './form.css'
import { useNavigate } from 'react-router-dom'
import { ACCESS_TOKEN, REFRESH_TOKEN } from '../../constants'
import api from '../../api'

export function Form({route, method}){
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [username, setUsername] = useState('')
    const [loading, setLoading] = useState(false)
    const navigate = useNavigate()

    const name = method === 'login' ? 'Login' : 'Register'

    const handleSubmit = async(e)=>{
        setLoading(true)
        e.preventDefault()

        try{
            
            const res = await api.post(route, {username, email, password });
            if(method === 'login'){
                localStorage.setItem(ACCESS_TOKEN, res.data.access)
                localStorage.setItem(REFRESH_TOKEN, res.data.refresh)
                navigate('/')
            }else{
                navigate('/login')
            }

        }

        catch(error) {
            if (error.response) {
                // The request was made, and the server responded with a status code outside of 2xx
                console.error("Error Response Data:", error.response.data); // Log error details from server
                console.error("Error Status Code:", error.response.status); // Log status code for better debugging
        
                alert(`Error ${error.response.status}: ${error.response.data.detail || 'Something went wrong'}`);
            } else if (error.request) {
                // The request was made, but no response was received
                console.error("No Response:", error.request);
                alert("No response received from server.");
            } else {
                // Something happened in setting up the request that triggered an error
                console.error("Error Message:", error.message);
                alert("Error: " + error.message);
            }
        }
        
        
        
        finally{
            setLoading(false)
        }
    }

    return (
        <form action="" onSubmit={handleSubmit}>
            <h1>{name}</h1>

            {method === 'register' && 
            <input
                type='text'
                value={username}
                onChange={(e)=> setUsername(e.target.value)}
                placeholder='Username'
            />}

            <input 
                type="email"
                value={email}
                onChange={(e)=> setEmail(e.target.value)}
                placeholder='Email'
            />

            <input 
                type="password"
                value={password}
                onChange={(e)=> setPassword(e.target.value)}
                placeholder='password'
            />

            <button type='submit'>{name}</button>
        </form>
    )
}