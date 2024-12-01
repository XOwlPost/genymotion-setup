# Port Allocation Plan

## **System & Network Services**
| **Service**        | **Default Port(s)** | **Description**                |
|---------------------|---------------------|---------------------------------|
| SSH                | 22                  | Secure shell access.           |
| HTTP               | 80                  | Standard web traffic.          |
| HTTPS              | 443                 | Secure web traffic.            |

## **NGINX & Proxies**
| **Service**        | **Default Port(s)** | **New Port(s)** | **Description**                      |
|---------------------|---------------------|-----------------|---------------------------------------|
| NGINX Proxy        | 80, 443, 6080       | 8080, 8443      | Reverse proxy for internal services. |
| Genymotion Emulator| 6080                | 8081            | Web interface for Genymotion.        |

## **Android Emulators (ADB)**
| **Instance**       | **Default Port(s)** | **New Port(s)** | **Description**                      |
|---------------------|---------------------|-----------------|---------------------------------------|
| Emulator 1         | 5554, 5555          | 5554, 5555      | Standard emulator for Android.       |
| Emulator 2         | N/A                 | 5556, 5557      | Future instance.                     |

## **Application Services**
| **Service**        | **Default Port(s)** | **New Port(s)** | **Description**                      |
|---------------------|---------------------|-----------------|---------------------------------------|
| AppAgent Webhook   | 5000                | 7000            | Manages external tasks & events.     |
| Database (Postgres)| 5432                | 5432            | Standard database connection.        |
| WebSocket (Future) | N/A                 | 9000            | Real-time communication.             |

## **Reserve Ports**
| **Range**          | **Purpose**         |
|---------------------|---------------------|
| 8000-8100          | Reserve for future use. |
