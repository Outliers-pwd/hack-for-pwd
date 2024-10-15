import { Children, useEffect } from "react"
import { useState } from "react"
import {ACCESS_TOKEN, REFRESH_TOKEN} from '../constants'
import { Navigate } from "react-router-dom"
import { jwtDecode } from "jwt-decode"

export function ProtectedRoute(){
    const [isAuthorized, setIsAuthorized] = useState(null)

    useEffect(()=>{
        auth().catch(()=>setIsAuthorized(false))
    }, [])

    const refreshToken = async()=>{
        const refreshToken = localStorage.getItem(REFRESH_TOKEN)
        try{
            const res = await api.post('/token/refresh/', {
                refresh: refreshToken
            })
            if (res.status === 200){
                localStorage.setItem(ACCESS_TOKEN, res.data.access)
                setIsAuthorized(true)
            }
            else{
                setIsAuthorized(false)
            }
        }
        catch(error){
            setIsAuthorized(false)
            Navigate('login/')
        }
    }

    const auth = async()=>{
        const token = localStorage.getItem(ACCESS_TOKEN)
        if(!token){
            setIsAuthorized(false)
            return
        }
        const decoded = jwtDecode(token)
        const tokenExpiration = decoded.exp
        const now = Date.now()/1000

        if(tokenExpiration< now){
            await(refreshToken)
        }
        else{
            setIsAuthorized(true)
        }
    }

    if(isAuthorized=== null){
        return <div>Loading</div>
    }
    return isAuthorized ? children : <Navigate to='/login'/> 
}