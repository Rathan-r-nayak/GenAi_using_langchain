from langchain.text_splitter import RecursiveCharacterTextSplitter,Language

text = """## Introduction
The human body continuously exchanges signals with the brain through the nervous system.  
If these electrical signals can be **captured, decoded, and translated into machine-readable form**, they can unlock an entirely new way of interacting with technology.  

This vision goes beyond eliminating keyboards, touchscreens, or voice commands—it creates a **direct bridge between human intent and machines**.

## The Ecosystem Vision

### 1. Signal Capture
- Non-invasive or minimally invasive devices placed at accessible points (e.g., neck, scalp, or wearable headbands)  
- Capture neural/electrical signals traveling between body and brain  
- Lightweight, real-time data collection without hindering natural body functions  

### 2. Signal Decoding & AI Translation
- Use advanced **AI/ML models** to translate raw neural patterns into:
  - Commands  
  - Emotions  
  - Sensory feedback  
- Adaptive systems that learn from each user’s unique signal patterns  

### 3. Machine Interaction
Once decoded, the signals can be used to control:
- **Smartphones & computers** (open apps, write messages, browse, code)  
- **Smart homes** (lights, fans, security systems, appliances)  
- **Vehicles & mobility aids** (wheelchairs, cars, drones)  
- **Industrial systems** (robotics, factory machines, medical equipment)  

### 4. Feedback Loop
- Machines can also send simplified signals back to the brain (through sensory pathways)  
- Enables two-way interaction, creating a **human-machine symbiosis**  

"""


splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=300,
    chunk_overlap = 0
)

chunks = splitter.split_text(text)
print(len(chunks))
for i in chunks:
    print("--------------------------------------")
    print(i)
