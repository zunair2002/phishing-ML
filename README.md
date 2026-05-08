

# Scan My Messages: AI-Powered Phishing Detector

## Introduction

Scan My Messages is a professional-grade cybersecurity web application engineered to protect users from the growing threat of SMS phishing, fraudulent scams, and malicious digital communication. In today’s world, cybercriminals use increasingly sophisticated social engineering tactics to steal personal data. This project addresses that challenge by providing a dual-layer verification system.

The application doesn't just tell you if a message is dangerous; it teaches you why. By combining traditional high-speed Machine Learning (Scikit-Learn) with state-of-the-art Generative AI (Groq/Llama 3), Scan My Messages analyzes linguistic patterns, urgency, and intent of a text to provide a comprehensive security verdict. This makes it an essential tool for both individual security and educational purposes in identifying modern phishing attempts.

---

## Key Features

* **Real-time Classification:** Instantly processes any text input to categorize it as "Spam/Malicious" or "Ham/Safe" using a high-performance ML pipeline.
* **AI-Driven Explainability:** Uses Groq Cloud (Llama 3.1) to generate natural language explanations highlighting red flags in messages.
* **Professional Cybersecurity UI:** A sleek, enterprise-inspired dashboard designed for clarity and usability.
* **Hybrid Security Architecture:** Combines Scikit-Learn ML model for fast classification and LLM for advanced reasoning.
* **Interactive Comparison Tool:** Visual learning cards to distinguish between malicious, suspicious, and safe messages.
* **Security First:** Environment-variable protection for API keys with a responsive, secure design across all devices.

---

## Frontend Stack

* React.js (Functional Components & Hooks)
* Tailwind CSS (Utility-first modern styling)
* Lucide React (Professional iconography)
* Framer Motion (Optional animations & transitions)

---

## Backend Stack

* Python Flask (REST API architecture)
* Scikit-Learn (Spam detection & vectorization model)
* Pickle Serialization (Model & vectorizer loading)
* Groq API (Llama 3.1-8b-instant for explanations)
* Python-Dotenv (Secure environment variable management)

