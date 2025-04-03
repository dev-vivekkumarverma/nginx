To handle **HTTPS** requests in Nginx, you need to:  
1. Obtain an **SSL certificate** (from Let's Encrypt, a certificate authority, or a self-signed cert).  
2. Configure an **HTTPS server block** in `nginx.conf`.  
3. Redirect HTTP to HTTPS (optional but recommended).  

---

## **1️⃣ Obtain an SSL Certificate**
### **Option 1: Using Let's Encrypt (Recommended)**
If your domain is **example.com**, install Certbot and get a free SSL certificate:  
```bash
sudo apt update
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d example.com -d www.example.com
```
Certbot automatically configures SSL in `nginx.conf`.  
**Renew the certificate automatically**:  
```bash
sudo certbot renew --dry-run
```

---

### **Option 2: Self-Signed Certificate (For Testing)**
If you don’t have a domain, create a **self-signed certificate**:
```bash
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/ssl/private/nginx-selfsigned.key \
    -out /etc/ssl/certs/nginx-selfsigned.crt
```

---

## **2️⃣ Configure Nginx for HTTPS**
Edit your **`nginx.conf`** or a virtual host file (`/etc/nginx/sites-available/default`):
```nginx
server {
    listen 80;
    server_name example.com www.example.com;
    return 301 https://$host$request_uri;  # Redirect HTTP to HTTPS
}

server {
    listen 443 ssl;
    server_name example.com www.example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;  # Use Certbot-generated cert
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    location / {
        root /var/www/html;
        index index.html;
    }
}
```
### **What This Does:**
✅ **Redirects HTTP to HTTPS**  
✅ **Enables SSL encryption**  
✅ **Secures the server with strong ciphers**  

---

## **3️⃣ Test & Restart Nginx**
Check the config:
```bash
sudo nginx -t
```
Restart Nginx:
```bash
sudo systemctl restart nginx
```

---

### **Final Notes**
- ✅ **If using AWS/GCP, open port `443` in security groups.**  
- ✅ **For high-security sites, enable `HSTS` (Strict Transport Security).**  
- ✅ **Use `certbot` to auto-renew certificates every 90 days.**  

Do you need **help with debugging SSL issues** or setting up **a reverse proxy with HTTPS**? 🚀