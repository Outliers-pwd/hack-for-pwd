import React from "react";
import { Outlet, Link } from "react-router-dom";
import { Navbar, Nav } from "react-bootstrap"; // Make sure this line is correct

export default function Layout() {
    return (
        <>
            <Navbar bg="light" expand="lg">
                <Navbar.Brand as={Link} to="/">My App</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <Nav.Link as={Link} to="/">Home</Nav.Link>
                        <Nav.Link as={Link} to="/login">Login</Nav.Link>
                        <Nav.Link as={Link} to="/register">Register</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>
            <div className="container mt-4">
                <Outlet />
            </div>
        </>
    );
}
