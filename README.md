🌱 AlgaeSense
Autonomous Algae Growing AI

AlgaeSense is an Edge-AI powered machine designed to monitor, understand and autonomously control algae growth.

Photobioreactors already provide the physical environment for growing algae. Our focus is the intelligence layer. AlgaeSense uses an Arduino UNO Q, a USB digital microscope, environmental sensors, computer vision and Edge AI to continuously observe the algae and determine what the growing system needs.
A peristaltic pump periodically moves a small sample of the culture into an imaging chamber, where the microscope captures images. The UNO Q processes these images locally to detect algae, estimate concentration, analyse growth and eventually identify contamination.
At the same time, AlgaeSense collects environmental information such as pH, dissolved CO₂, turbidity, TDS, temperature and humidity. This information is combined with the vision system to control LED lighting, aeration, agitation, nutrient dosing, cooling and eventually harvesting.
The basic idea is:
                    ALGAE
                      ↓
              🔬 USB Microscope
                      ↓
              🧠 Edge AI / CV
                      ↓
             "What is happening?"
                      ↓
        ┌─────────────┴─────────────┐
        ↓                           ↓
   Environmental               Growth analysis
     Sensors                        ↓
        └─────────────┬─────────────┘
                      ↓
               Control Algorithm
                      ↓
        ┌───────┬─────┼─────┬───────┐
        ↓       ↓     ↓     ↓       ↓
       LEDs   Air   Agitate Nutrients Harvest
The important distinction: AI is not replacing the photobioreactor. AI is turning the photobioreactor into an autonomous system.
The long-term vision is to make this intelligence modular enough to operate different reactor designs, from small hobby systems and educational setups to laboratories, farms and industrial cultivation systems, with changes mainly to operating parameters and hardware interfaces.

To Summarize it : 
AlgaeSense gives an algae-growing system eyes, sensors and a brain — so it can monitor and grow algae without a scientist constantly standing beside it.
