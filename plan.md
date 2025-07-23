# Plan to Enhance Bot User Experience

My primary goal is to make the bot more intuitive, user-friendly, and modern by leveraging the latest `aiogram` features.

### 1. Improve Command Discovery with `set_my_commands`
*   **What:** I'll register all bot commands with Telegram so they appear in the command menu (the "/" button).
*   **Why:** This makes it easy for users to see what the bot can do without having to guess or remember commands.
*   **How:** I'll create a `utils/commands.py` file to define the commands and call it on startup in `bot.py`.

### 2. Create a Comprehensive `/help` Command
*   **What:** The current `/help` is minimal. I'll create a new, detailed help message.
*   **Why:** A good help command is essential for a good user experience, explaining what each feature does.
*   **How:** I'll add a new handler in `handlers/user_commands.py` that sends a formatted message with explanations for all commands and features.

### 3. Redesign Keyboards for Clarity and Ease of Use
*   **What:** I'll replace the current cryptic keyboard buttons (`sttngs`, `mdl`, etc.) with clear text and emojis (`⚙️ Settings`, `🤖 Model`).
*   **Why:** This makes the interface much more intuitive and visually appealing.
*   **How:** I'll refactor all keyboards in `keyboards/inline.py` using `InlineKeyboardBuilder` and add a "⬅️ Back" button to all sub-menus for easy navigation.

### 4. Enhance Bot's Responses
*   **What:** I'll review and improve the text the bot sends back to the user.
*   **Why:** Clear and informative feedback makes the bot feel more responsive and helpful.
*   **How:** I'll update the messages in the handlers to be more descriptive (e.g., "Parameter 'steps' updated to 50.").

### 5. Update Handlers and Logic
*   **What:** I'll update the code that handles button clicks to work with the new keyboards.
*   **Why:** This is necessary to make the new interface functional.
*   **How:** I'll modify the callback handlers in `handlers/callbacks.py` to match the new callback data from the redesigned keyboards.

### User Flow Diagram

```mermaid
graph TD
    A[User] -->|/start or /help| B(Bot: Welcome & Main Menu);
    B --> C{Main Keyboard};
    C -->|⚙️ Settings| D[Settings Menu];
    C -->|📜 Scripts| E[Scripts Menu];
    C -->|🎨 Generate| F[Generate Image];
    C -->|⏭️ Skip| G[Skip Generation];
    C -->|❓ Help| H[Show Help];

    D -->|Change Parameter| I[Select Parameter];
    D -->|Reset Parameters| J[Reset to Default];
    D -->|Fast Presets| K[Select Preset];
    D -->|⬅️ Back| C;

    I -->|Selects Param| L[Enter New Value];
    L -->|Enters Value| D;

    K -->|Selects Preset| D;

    E -->|Get LORA| M[Display LORA list];
    E -->|Random Model| N[Run Random Model Script];
    E -->|Random Sampler| O[Run Random Sampler Script];
    E -->|Infinite Generation| P[Run Infinite Script];
    E -->|⬅️ Back| C;

    M --> E;
    N --> E;
    O --> E;
    P --> E;