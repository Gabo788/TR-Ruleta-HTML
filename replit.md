# Ruleta Casino - Educational Roulette Game

## Overview

An interactive educational roulette casino game built with Flask that teaches concepts of probability and statistics, specifically the gambler's fallacy. The application simulates a roulette wheel where users can place bets on numbers or colors, with a deliberate mechanic where the first 9 spins always land on red to demonstrate probability misconceptions.

**Core Purpose:** Educational tool for understanding probability, randomness, and the gambler's fallacy through an engaging casino game interface.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Architecture

**Framework:** Flask 3.0.0  
**Language:** Python  
**Pattern:** Simple MVC-style structure

The application uses a straightforward Flask architecture with separated concerns:

- **app.py** - Main Flask application handling HTTP routes and request/response logic
- **ruleta.py** - Core game logic module containing roulette mechanics and betting system

**Key Architectural Decisions:**

1. **Separation of Game Logic**  
   - Problem: Keep business logic separate from web layer
   - Solution: Isolated `ruleta.py` module for all game mechanics
   - Rationale: Enables testing game logic independently and potential reuse in other contexts

2. **Stateless Request Handling**  
   - Problem: Track game state across multiple spins
   - Solution: Client-side state management, server receives `numero_tirada` parameter
   - Pros: Simple server architecture, no session management needed
   - Cons: Client could manipulate spin count (acceptable for educational purposes)

3. **Educational Bias Implementation**  
   - Problem: Demonstrate gambler's fallacy effectively
   - Solution: First 9 spins programmatically fixed to red numbers
   - Rationale: Creates pattern that tempts users to make false predictions, teaching moment about independent probability

### Frontend Architecture

**Technologies:** HTML5, CSS3, Vanilla JavaScript (implied from incomplete template)  
**Pattern:** Client-side rendering with AJAX calls

**Key Features:**
- Visual roulette wheel interface
- Chip selection system (€0.20, €0.50, €1, €5)
- Dual betting modes (numbers and colors)
- Real-time balance tracking
- Spin counter display

**State Management:**
- Client maintains game state (balance, spin count, selected chip)
- Server only processes individual bet calculations

### Game Mechanics

**Roulette Simulation:**
- Standard European roulette (0-36)
- Red numbers: 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36
- Black numbers: 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35
- Green: 0

**Betting System:**
- Number bet: 36x payout
- Color bet: 2x payout
- Educational bias: Spins 1-9 always land on red

**API Design:**

**POST /girar**
- Input: `tipo_apuesta` (numero/color), `valor_apuesta` (number or color), `ficha` (bet amount), `numero_tirada` (spin count)
- Output: `numero` (winning number), `color` (winning color), `ganancia` (multiplier), `ganancia_euros` (euro winnings)

### Deployment Architecture

**Platform:** Vercel (configured)  
**Runtime:** Python on serverless functions

**Configuration Strategy:**
- Vercel builder for Python applications
- Static file serving for CSS/JS assets
- Catch-all route to Flask app

**Rationale:** Serverless deployment provides:
- Zero infrastructure management
- Automatic scaling
- Free tier suitable for educational projects

## External Dependencies

### Backend Dependencies
- **Flask 3.0.0** - Web framework for routing and request handling

### Deployment Platform
- **Vercel** - Serverless hosting platform with Python runtime support (@vercel/python builder)

### Built-in Python Modules
- **random** - Random number generation for roulette spins

**Note:** The application is intentionally lightweight with minimal dependencies to maintain simplicity and educational focus. No database, authentication, or external APIs are used, keeping the architecture simple and self-contained.