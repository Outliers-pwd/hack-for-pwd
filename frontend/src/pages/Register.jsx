import React, { useState } from "react";
import axios from "axios";
import { Form, Button, Alert } from "react-bootstrap"; // Import Bootstrap components

export default function Register() {
    const [formData, setFormData] = useState({
        username: "",
        email: "",
        password1: "",
        password2: "",
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

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (isLoading) return;

        // Validate password match
        if (formData.password1 !== formData.password2) {
            setErrorMessages(["Passwords do not match!"]);
            return;
        }

        setIsLoading(true);
        setErrorMessages([]); // Clear previous errors

        try {
            const response = await axios.post("http://127.0.0.1:8000/api/register/", formData);
            console.log("Success!", response.data);
            setSuccessMessage("Registration Successful!");
            // Optionally clear the form
            setFormData({
                username: "",
                email: "",
                password1: "",
                password2: "",
            });
        } catch (error) {
            console.log("Error during registration!", error.response?.data);
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
            <h2>Register:</h2>
            <Form onSubmit={handleSubmit}>
                <Form.Group controlId="formUsername">
                    <Form.Label>Username</Form.Label>
                    <Form.Control
                        type="text"
                        name="username"
                        value={formData.username}
                        onChange={handleChange}
                        placeholder="Enter your username"
                        required
                    />
                </Form.Group>

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

                <Form.Group controlId="formPassword1">
                    <Form.Label>Password</Form.Label>
                    <Form.Control
                        type="password"
                        name="password1"
                        value={formData.password1}
                        onChange={handleChange}
                        placeholder="Enter your password"
                        required
                    />
                </Form.Group>

                <Form.Group controlId="formPassword2">
                    <Form.Label>Confirm Password</Form.Label>
                    <Form.Control
                        type="password"
                        name="password2"
                        value={formData.password2}
                        onChange={handleChange}
                        placeholder="Confirm your password"
                        required
                    />
                </Form.Group>

                <Button variant="primary" type="submit" disabled={isLoading} className="mt-3">
                    {isLoading ? "Registering..." : "Register"}
                </Button>
            </Form>
        </div>
    );
}
