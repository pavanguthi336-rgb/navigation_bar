<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Landing Page</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Poppins', sans-serif;
        }
        
        body {
            scroll-behavior: smooth;
        }
        /* Navigation Bar */
        
        nav {
            position: fixed;
            width: 100%;
            top: 0;
            left: 0;
            background: transparent;
            padding: 20px 50px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: 0.3s;
            z-index: 1000;
        }
        
        nav.scrolled {
            background: #111;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.4);
        }
        
        nav .logo {
            color: #fff;
            font-size: 24px;
            font-weight: bold;
        }
        
        nav ul {
            list-style: none;
            display: flex;
            gap: 20px;
        }
        
        nav ul li a {
            text-decoration: none;
            color: #fff;
            font-size: 18px;
            transition: 0.3s;
        }
        
        nav ul li a:hover {
            color: #00bcd4;
            border-bottom: 2px solid #00bcd4;
            padding-bottom: 4px;
        }
        /* Hero Section */
        
        section {
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            color: white;
            background: linear-gradient(120deg, #1e1e2f, #232334);
            text-align: center;
            padding: 20px;
        }
        
        section h1 {
            font-size: 48px;
            margin-bottom: 20px;
        }
        
        section p {
            font-size: 20px;
            max-width: 600px;
        }
        /* Responsive */
        
        @media (max-width: 768px) {
            nav ul {
                flex-direction: column;
                background: rgba(0, 0, 0, 0.8);
                position: absolute;
                top: 70px;
                right: 20px;
                padding: 10px;
                border-radius: 8px;
                display: none;
            }
            nav ul.active {
                display: block;
            }
            .menu-toggle {
                display: block;
                color: #fff;
                font-size: 28px;
                cursor: pointer;
            }
        }
        
        .menu-toggle {
            display: none;
        }
    </style>
</head>

<body>
    <nav id="navbar">
        <div class="logo">SkillCraft</div>
        <div class="menu-toggle" id="menu-toggle">&#9776;</div>
        <ul id="nav-links">
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <section id="home">
        <h1>Responsive Landing Page</h1>
        <p>Create an interactive navigation menu that changes style when scrolled or hovered.</p>
    </section>

    <section id="about" style="background:#2c2c3e;">
        <h1>About Us</h1>
        <p>We build beautiful, responsive web applications with interactive designs.</p>
    </section>

    <section id="services" style="background:#1c1c28;">
        <h1>Our Services</h1>
        <p>Web Development, UI/UX Design, AI Solutions, and more.</p>
    </section>

    <section id="contact" style="background:#2c2c3e;">
        <h1>Contact Us</h1>
        <p>Email: contact@skillcraft.com | Phone: ‪+91 98765 43210‬</p>
    </section>

    <script>
        // Change nav style when scrolling
        window.addEventListener('scroll', function() {
            const navbar = document.getElementById('navbar');
            navbar.classList.toggle('scrolled', window.scrollY > 50);
        });

        // Toggle menu for small screens
        const toggle = document.getElementById('menu-toggle');
        const navLinks = document.getElementById('nav-links');

        toggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    </script>
</body>

</html>