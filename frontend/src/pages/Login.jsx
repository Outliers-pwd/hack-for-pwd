import React, { useState } from "react";
import axios from "axios";
import { Form, Button, Alert } from "react-bootstrap"; // Import Bootstrap components
import { useNavigate } from "react-router-dom"; // Import useNavigate for redirecting

export default function Login() {
    const [formData, setFormData] = useState({
        email: "",
        password: "",
    });

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
    };

    const [isLoading, setIsLoading] = useState(false);
    const [successMessage, setSuccessMessage] = useState(null);
    const [errorMessages, setErrorMessages] = useState([]);
    const navigate = useNavigate(); // Initialize useNavigate

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (isLoading) return;

        setIsLoading(true);
        setErrorMessages([]); // Clear previous errors

        try {
            const response = await axios.post("http://127.0.0.1:8000/api/login/", formData);
            console.log("Success!", response.data);
            setSuccessMessage("Login Successful!");
            localStorage.setItem("accessToken", response.data.tokens.access);
            localStorage.setItem("refreshToken", response.data.tokens.refresh);

            // Redirect to a different page after successful login
            navigate("/dashboard"); // Change to your desired route
        } catch (error) {
            console.log("Error during Login!", error.response?.data);
            if (error.response && error.response.data) {
                const errors = Object.values(error.response.data).flat(); // Collect all error messages
                setErrorMessages(errors);
            }
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="container mt-4">
            {errorMessages.length > 0 && (
                <Alert variant="danger">
                    {errorMessages.map((msg, index) => (
                        <div key={index}>{msg}</div>
                    ))}
                </Alert>
            )}
            {successMessage && <Alert variant="success">{successMessage}</Alert>}
            <h2>Login:</h2>
            <Form onSubmit={handleSubmit}>
                <Form.Group controlId="formEmail">
                    <Form.Label>Email</Form.Label>
                    <Form.Control
                        type="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                        placeholder="Enter your email"
                        required
                    />
                </Form.Group>

                <Form.Group controlId="formPassword">
                    <Form.Label>Password</Form.Label>
                    <Form.Control
                        type="password"
                        name="password"
                        value={formData.password}
                        onChange={handleChange}
                        placeholder="Enter your password"
                        required
                    />
                </Form.Group>

                <Button variant="primary" type="submit" disabled={isLoading} className="mt-3">
                    {isLoading ? "Logging in..." : "Login"}
                </Button>
            </Form>
        </div>
    );
}
