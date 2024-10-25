import React, { useState } from 'react';
import { Button } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';

const OnboardingWizard = () => {
    const [step, setStep] = useState(0);
    const [preferences, setPreferences] = useState({
        disabilityType: '',
        goals: [],
        devices: [],
        reminders: [],
    });
    const navigate = useNavigate();

    const nextStep = () => {
        setStep(step + 1);
    };

    const previousStep = () => {
        setStep(step - 1);
    };

    const handlePreferenceChange = (key, value) => {
        setPreferences((prev) => ({ ...prev, [key]: value }));
    };

    const handleFinish = () => {
        // Handle the completion of onboarding
        console.log(preferences);
        navigate('/'); // Navigate to home or any other page
    };

    const renderStep = () => {
        switch (step) {
            case 0:
                return (
                    <div>
                        <h3>Select Disability Type</h3>
                        <select onChange={(e) => handlePreferenceChange('disabilityType', e.target.value)}>
                            <option value="">Select...</option>
                            <option value="visual">Visual</option>
                            <option value="hearing">Hearing</option>
                            <option value="mobility">Mobility</option>
                            {/* Add more options as needed */}
                        </select>
                    </div>
                );
            case 1:
                return (
                    <div>
                        <h3>Select Your Goals</h3>
                        <input
                            type="checkbox"
                            value="fitness"
                            onChange={(e) => handlePreferenceChange('goals', [...preferences.goals, e.target.value])}
                        />
                        Fitness
                        <input
                            type="checkbox"
                            value="mentalHealth"
                            onChange={(e) => handlePreferenceChange('goals', [...preferences.goals, e.target.value])}
                        />
                        Mental Health
                        <input
                            type="checkbox"
                            value="diet"
                            onChange={(e) => handlePreferenceChange('goals', [...preferences.goals, e.target.value])}
                        />
                        Diet
                    </div>
                );
            case 2:
                return (
                    <div>
                        <h3>Devices Used</h3>
                        <input
                            type="text"
                            placeholder="e.g. wheelchair"
                            onChange={(e) => handlePreferenceChange('devices', e.target.value)}
                        />
                    </div>
                );
            case 3:
                return (
                    <div>
                        <h3>Set Reminders</h3>
                        <input
                            type="checkbox"
                            value="waterIntake"
                            onChange={(e) => handlePreferenceChange('reminders', [...preferences.reminders, e.target.value])}
                        />
                        Water Intake
                        <input
                            type="checkbox"
                            value="workouts"
                            onChange={(e) => handlePreferenceChange('reminders', [...preferences.reminders, e.target.value])}
                        />
                        Workouts
                        <input
                            type="checkbox"
                            value="meditation"
                            onChange={(e) => handlePreferenceChange('reminders', [...preferences.reminders, e.target.value])}
                        />
                        Meditation
                    </div>
                );
            default:
                return (
                    <div>
                        <h3>Review Your Preferences</h3>
                        <pre>{JSON.stringify(preferences, null, 2)}</pre>
                        <Button onClick={handleFinish}>Finish</Button>
                    </div>
                );
        }
    };

    return (
        <div className="onboarding-wizard">
            {renderStep()}
            <div className="mt-4">
                {step > 0 && <Button variant="secondary" onClick={previousStep}>Back</Button>}
                {step < 4 && <Button variant="primary" onClick={nextStep}>Next</Button>}
            </div>
        </div>
    );
};

export default OnboardingWizard;
