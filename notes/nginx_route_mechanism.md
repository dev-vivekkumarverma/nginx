
### ⚙️ Load Balancing Mechanisms in NGINX

#### 1. **Round Robin** (default – no keyword needed)

Distributes requests one-by-one in order.

```nginx
upstream backend_servers {
    server server_01:8000;
    server server_02:8000;
    server server_03:8000;
}
```

---

#### 2. **Least Connections**

Chooses the server with the fewest active connections.

```nginx
upstream backend_servers {
    least_conn;
    server server_01:8000;
    server server_02:8000;
    server server_03:8000;
}
```

---

#### 3. **IP Hash**

Same client IP always hits the same backend (good for session stickiness).

```nginx
upstream backend_servers {
    ip_hash;
    server server_01:8000;
    server server_02:8000;
    server server_03:8000;
}
```

---

#### 4. **Weighted Round Robin**

Assign more traffic to stronger servers.

```nginx
upstream backend_servers {
    server server_01:8000 weight=3;
    server server_02:8000 weight=2;
    server server_03:8000 weight=1;
}
```

---

### ✅ Full Example with `least_conn`:

```nginx
http {
    upstream backend_servers {
        least_conn;
        server server_01:8000;
        server server_02:8000;
        server server_03:8000;
    }

    server {
        listen 80;

        location / {
            proxy_pass http://backend_servers;
        }
    }
}
```

---

### 📌 Summary Table

| Method         | Keyword     | Use Case                            |
|----------------|-------------|-------------------------------------|
| Round Robin    | *(default)* | Even distribution                   |
| Least Conn     | `least_conn`| Long-running or heavy requests      |
| IP Hash        | `ip_hash`   | Sticky sessions (same IP to same backend) |
| Weighted       | `weight=x`  | Some backends are more powerful     |

---

The `weight=x` parameter in NGINX load balancing is used to **control how much traffic each backend server gets** relative to the others. This is part of the **weighted round robin** mechanism.

---

### 🏋️‍♂️ What Does `weight=x` Mean?

- Each server is assigned a **weight**.
- The **higher the weight**, the **more requests** it will receive.
- Default weight is `1` if you don’t specify it.

---

### ✅ Example

```nginx
upstream backend_servers {
    server server_01:8000 weight=5;
    server server_02:8000 weight=3;
    server server_03:8000 weight=1;
}
```

**What this does:**
- For every **9 requests**, NGINX sends:
  - 5 to `server_01`
  - 3 to `server_02`
  - 1 to `server_03`

This is ideal when:
- You have backend containers or machines with **different processing power or capacity**.
- You want to **control the load distribution manually**.

---

### ⚠️ Important Notes

- `weight=` only works with **round robin** (default). Don't mix it with `least_conn` or `ip_hash`.
- You can assign any positive integer value.

