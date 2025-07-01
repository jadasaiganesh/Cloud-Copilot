# 🚀 CloudCopilot  
*A Full-Stack Django Platform to Learn AWS & Simulate a Cloud Dashboard*

---

## 📘 Project Overview

CloudCopilot is an interactive, educational Django-based web platform designed to simulate AWS cloud service management for learners and developers.

It provides:
- 🎨 Responsive Django + Bootstrap UI  
- 🔐 Secure login system with OTP password reset  
- 💾 CSRF/session protection  
- ☁️ Deployment on AWS EC2  
- 🗂️ Complete GitHub version control  

---

## 🎯 Objectives

| Goal                | Description                                            |
|---------------------|--------------------------------------------------------|
| 🎓 Learn AWS        | Simplified interface to understand services like EC2, S3 |
| 🔐 Build Full-Stack App | Backend, frontend, authentication, and deployment      |
| 🖥️ Simulate Cloud Console | Mimics real AWS dashboard behavior                   |
| 🛡️ Practice Secure Coding | CSRF, OTP, sessions, SMTP integration              |
| 🚀 Deploy on AWS     | Uses EC2 instance with SSH + Git + Django stack        |

---

## 🧠 Key Features

### ✅ 1. User Authentication
- Uses Django’s built-in user model  
- Supports registration, login, and logout  
- Routes protected using `@login_required`  

### ✅ 2. Password Reset via OTP (SMTP)
- Users request a password reset via email  
- 6-digit OTP sent using Django’s `send_mail()`  
- OTP verified before password reset allowed  
- SMTP credentials stored securely in `settings.py`  

### ✅ 3. AWS Learning Dashboard
Each AWS service (EC2, S3, IAM, Lambda) has its own page that includes:
- 📄 Definition  
- 💡 Use Case  
- 🖼️ Illustration  
- 🔗 Link to official AWS documentation  

### ✅ 4. Mobile-Responsive UI
- Built using Bootstrap 5  
- Navbar and cards adapt for smaller devices  
- Toggle menu and layout scale fluidly  

### ✅ 5. Secure Architecture

| Security Feature     | Implementation                                    |
|----------------------|--------------------------------------------------|
| CSRF Protection      | `{% csrf_token %}` in all forms                  |
| Session Security     | Django's session middleware                      |
| SMTP OTP             | Secure session-based OTP system                  |
| Route Protection     | `@login_required` decorators                     |

---

## 🛠️ Tech Stack

| Layer           | Tools Used                          |
|------------------|-------------------------------------|
| Backend          | Python, Django                      |
| Frontend         | HTML5, CSS3, Bootstrap 5, Icons     |
| Database         | SQLite (extendable to PostgreSQL)   |
| Authentication   | Django Auth + OTP (SMTP)            |
| Version Control  | Git, GitHub                         |
| Deployment       | AWS EC2, SSH                        |

---

## 📁 Project Structure

<pre>
cloudcopilot/
├── accounts/
│   ├── templates/accounts/
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── forgot_password.html
│   │   └── reset_password.html
│   ├── views.py
│   ├── urls.py
├── dashboard/
│   ├── templates/dashboard/
│   │   ├── home.html
│   │   ├── services.html
│   │   ├── about.html
│   │   ├── profile.html
│   │   ├── ec2.html
│   │   ├── s3.html
│   │   ├── iam.html
│   │   └── lambda.html
│   ├── views.py
│   ├── urls.py
├── cloudcopilot/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── staticfiles/
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
</pre>

---

## 🔗 User Flow

### 🔐 Registration / Login
- Secure registration and login via Django’s auth system  
- Protected views using `@login_required`  
- Redirects users to the dashboard upon login  

### 🔁 Forgot Password?
- User enters registered email  
- 6-digit OTP sent via SMTP  
- After OTP verification, user resets password  

### 📚 AWS Service Explorer
- Dashboard shows clickable cards for EC2, S3, IAM, Lambda  
- Each card opens a page with explanation, use case, and diagrams  

### 👤 Profile Page
- Displays user information  

### 🚪 Logout
- Logs out user and clears session  

---

## 🌍 Deployment Guide

### ✅ Prerequisites
- AWS EC2 instance (Ubuntu)
- Python 3, pip, venv, and git installed

### 🧩 Setup Steps

```bash
# 1. Connect to EC2
ssh -i cloudcopilot.pem ubuntu@<EC2_PUBLIC_IP>

# 2. Install necessary packages
sudo apt update
sudo apt install python3-pip python3-venv git

# 3. Clone the project
git clone https://github.com/jadasaiganesh/Cloud-Copilot.git
cd Cloud-Copilot

# 4. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# 5. Install dependencies
pip install -r requirements.txt

# 6. Run the server
python3 manage.py runserver 0.0.0.0:8000

✅ Access the app at: http://<EC2_PUBLIC_IP>:8000
```

---

## 🔐 Security Details

| Feature              | Description                                                  |
|----------------------|--------------------------------------------------------------|
| **OTP Verification** | Session-based, 6-digit email OTP sent via SMTP               |
| **CSRF Protection**  | Enabled via `{% csrf_token %}` in all POST forms             |
| **SMTP Configuration** | Credentials stored securely in `settings.py`              |
| **Access Restrictions** | Views protected by `@login_required`; admin via superuser |

---

## 📚 Resources & References

- [AWS Official Documentation](https://docs.aws.amazon.com/)
- [Django Official Documentation](https://docs.djangoproject.com/)
- **YouTube Channels**:
  - [Traversy Media](https://www.youtube.com/c/TraversyMedia)
  - [CodeWithHarry](https://www.youtube.com/c/CodeWithHarry)
  - [Kunal Kushwaha](https://www.youtube.com/c/KunalKushwaha)
- AWS Console (used for UI/UX inspiration)

---

## 🔧 Future Enhancements

| Feature            | Description                                                      |
|--------------------|------------------------------------------------------------------|
| 🔐 **HTTPS**       | Use Certbot + Nginx for secure HTTPS deployment                  |
| 💬 **Contact Form**| Allow users to send feedback with optional email notification    |
| 📊 **Admin Analytics** | Track user login activity and page views                    |
| 🐳 **Docker**      | Containerize app for consistent deployment                       |
| ⚙️ **CI/CD**       | Automate deployment via GitHub Actions                           |
| 📡 **AWS SDK**     | Connect to real AWS services using the `boto3` Python SDK        |

---

## 👨‍💻 Author & Vision

**Author**: Sai Ganesh  
**GitHub**: [@jadasaiganesh](https://github.com/jadasaiganesh)  
**Year**: 2025  

> _“Build secure, scalable, and educational platforms that teach by doing.”_
