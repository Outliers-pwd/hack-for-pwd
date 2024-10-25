// src/App.js

import './App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Layout from './pages/Layout';
import Register from './pages/Register';
import Login from './pages/Login';
import 'bootstrap/dist/css/bootstrap.min.css';
import OnboardingWizard from './components/OnboardingWizard';
import Dashboard from './components/Dashboard'; // Import your Dashboard component

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="login" element={<Login />} />
          <Route path="register" element={<Register />} />
          <Route path="/onboarding" element={<OnboardingWizard />} />
          <Route path="/dashboard" element={<Dashboard />} /> {/* Added route for Dashboard */}
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
