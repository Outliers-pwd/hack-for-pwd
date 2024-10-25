import React from "react";
import { Link } from "react-router-dom";
import { Button } from "react-bootstrap";

export default function Home() {
    return (
        <div className="text-center mt-5">
            {/* App Logo */}
            <img src="/ww1.png" alt="Wellness App Logo" className="mb-4" style={{ width: '200px' }} />

            {/* Tagline */}
            <h2 className="mb-4">Empowering Your Wellness Journey</h2>

            {/* Buttons */}
            <div className="d-flex justify-content-center gap-3">
                <Button as={Link} to="/register" variant="primary">
                    Register
                </Button>
                <Button as={Link} to="/login" variant="secondary">
                    Login
                </Button>
                <Button as={Link} to="/" variant="outline-primary">
                    Continue as Guest
                </Button>
                <Button as={Link} to="/onboarding" variant="success">
                    Get Started
                </Button>
                <Button as={Link} to="/dashboard" variant="success">
    Go to Dashboard
</Button>
            </div>
        </div>
    );
}
