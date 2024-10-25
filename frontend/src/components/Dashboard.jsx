// src/components/Dashboard.js

import React from 'react';
import { Button, Card, ProgressBar, Row, Col } from 'react-bootstrap';
import './Dashboard.css'; // Assume you will create a CSS file for styles

const Dashboard = () => {
    // Sample data
    const activitySummary = {
        activity: 120, // minutes
        nutrition: 3, // meals logged
        wellnessCheckins: 5, // number of check-ins
    };

    const fitnessGoalProgress = 75; // in percentage
    const mentalHealthGoalProgress = 60; // in percentage

    const appointments = [
        { time: '2024-10-26 10:00 AM', description: 'Telehealth with Dr. Smith' },
        { time: '2024-10-27 1:00 PM', description: 'Therapy Session with Jane Doe' },
    ];

    return (
        <div className="dashboard container mt-5">
            <h1 className="text-center">Welcome Back!</h1>
            
            {/* Daily Summary Section */}
            <Card className="mb-4">
                <Card.Body>
                    <Card.Title>Daily Summary</Card.Title>
                    <Row>
                        <Col>
                            <h5>Activity: {activitySummary.activity} mins</h5>
                        </Col>
                        <Col>
                            <h5>Nutrition: {activitySummary.nutrition} meals</h5>
                        </Col>
                        <Col>
                            <h5>Wellness Check-ins: {activitySummary.wellnessCheckins}</h5>
                        </Col>
                    </Row>
                </Card.Body>
            </Card>

            {/* Quick Actions Section */}
            <div className="d-flex justify-content-around mb-4">
                <Button variant="primary">Start Workout</Button>
                <Button variant="success">Log a Meal</Button>
                <Button variant="info">Join Community Chat</Button>
            </div>

            {/* Progress Section */}
            <Card className="mb-4">
                <Card.Body>
                    <Card.Title>Progress</Card.Title>
                    <h5>Fitness Goal</h5>
                    <ProgressBar now={fitnessGoalProgress} label={`${fitnessGoalProgress}%`} />
                    <h5>Mental Health Goal</h5>
                    <ProgressBar now={mentalHealthGoalProgress} label={`${mentalHealthGoalProgress}%`} />
                </Card.Body>
            </Card>

            {/* Upcoming Appointments Section */}
            <Card>
                <Card.Body>
                    <Card.Title>Upcoming Appointments</Card.Title>
                    {appointments.length === 0 ? (
                        <p>No upcoming appointments</p>
                    ) : (
                        appointments.map((appointment, index) => (
                            <div key={index} className="appointment">
                                <p><strong>{appointment.time}</strong>: {appointment.description}</p>
                            </div>
                        ))
                    )}
                </Card.Body>
            </Card>
        </div>
    );
};

export default Dashboard;
