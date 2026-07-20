# CampusConnect Notifications Service Design Document

## 1. High-Level Design

**Main Components/Modules:**
- Notification Generation Module: Detects events (new assignment, enrollment change) and creates notification objects.
- User Preferences Module: Stores and retrieves user notification settings (email, SMS, in-app).
- Delivery Module: Handles actual sending via different channels.
- Notification Database: Stores notification history and status.
- Event Bus: Decouples event producers from consumers.

**Layered Architecture (for the Student Portal + Notifications):**
- **Presentation Layer**: Handles UI (web/mobile app). Receives user preferences and displays notifications. Passes user actions to Business Layer.
- **Business Layer**: Contains core logic — generates notifications when events occur, checks user preferences, and decides delivery channels. Receives event from Event Bus and passes formatted notification to Delivery Layer.
- **Data Access Layer**: Interacts with the database to save notification history, fetch user preferences, and query events. Receives requests from Business Layer and returns data objects.
- **Database Layer**: Stores persistent data (notifications, preferences, events).

**Notification Event Flow:**
1. New assignment posted → Event Bus notifies Generation Module.
2. Generation Module creates Notification object and checks preferences (Business Layer).
3. Business Layer sends formatted notification to Delivery Module.
4. Delivery Module sends via chosen channel (email/SMS) and saves status via Data Access Layer.

## 2. Architectural Style Choice

**Chosen Style: Event-Driven Architecture**

**Advantages:**
1. Loose coupling between course/enrollment system and notifications — new assignment event can trigger notifications without direct calls.
2. High scalability — can process thousands of notifications asynchronously during peak times.
3. Easy to add new notification types (push, WhatsApp) without changing core modules.

**Challenges:**
1. Event ordering and eventual consistency issues (student might see notification delay).
2. Debugging distributed events is harder than in monolithic systems.

## 3. Low-Level Design

**Class 1: Notification**
- Attributes: notification_id (String), student_id (String), type (String), message (String), timestamp (DateTime), status (String)
- Methods: 
  - createNotification(student_id, type, message) → Notification
  - markAsRead() → void
- SOLID: Single Responsibility Principle (only handles notification data and status, not delivery).

**Class 2: NotificationDispatcher**
- Attributes: deliveryChannels (List<DeliveryChannel>)
- Methods: 
  - dispatch(Notification n) → boolean
  - registerChannel(channel) → void
- SOLID: Open/Closed Principle (can add new delivery channels without modifying dispatcher).

**Interface: DeliveryChannel**
- send(Notification n) → boolean
- getChannelType() → String

This interface allows swapping email, SMS, or push notification implementations without changing the Dispatcher (Dependency Inversion Principle).

## 4. Scalability Plan

**Bottleneck**: High notification delivery volume during peak enrollment/result days (thousands of events per minute).

**Scaling Choice**: Horizontal scaling (add more delivery worker instances).

**Elasticity Policy**: Auto-scale up when queue length > 500 notifications or CPU > 70%; scale down when queue is empty for 10 minutes.

**Load-Balancing Algorithm**: Least Connection — suitable because notification tasks have variable processing time (some emails take longer).

## 5. Cloud Deployment Recommendation

**Deployment Model**: Public Cloud  
**Justification (NIST)**: On-demand self-service and rapid elasticity allow quick scaling during exam periods without upfront hardware purchase.

**Service Model**: PaaS  
**Challenge Mitigated**: Limited control — PaaS provider manages underlying infrastructure and scaling, reducing operational burden while still allowing custom code deployment.

This combination gives CampusConnect fast scaling and reduced management overhead for the notifications service.
