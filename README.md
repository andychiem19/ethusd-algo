> [!NOTE]
> This project is a work-in-progress!

### Hardware-Accelerated Ethereum Trading System
The goal of this project is to port live data from a public crypto exchange's API (OKX) onto an FPGA using Python and UART, execute a highly efficient trading algorithm on hardware using SystemVerilog, and then return technical/trading analysis insights to the user on the software side. The ultimate goal is to use machine learning and hardware acceleration to create a profitable high-frequency trading system for Ethereum.

**Tools Used**

`Xilinx Vivado`
`Verilog/SystemVerilog`
`Python`
`Visual Studio Code`
`Git`

---

#### **Demos**

TBC

---

#### **Learning Objectives**

- **Real-time data handling** – Extract, encode, and make accurate decisions based on rapidly changing live data
- **UART communication** – Interface between software and hardware using UART
- **UI/UX** - Develop a basic user interface and user experience for those who wish to use the trading system
- **Hardware Acceleration** – Use hardware to implement more complex trading strategies than would be possible and time efficient on software, proving utility over fully software-based approaches to algorithmic trading
- **Algorithmic Trading Logic** – Through trade simulation and some form of iteration, extract value from the market systematically

---

#### **File Structure**

`/fpga` –> RTL files and Xilinx constraints files for hardware-side\
`/src` –> Software-side files for real-time data processing in Python

---

#### **Project Timeline & Features**

| Timeline | Feature | Description |
|--------|-------------|--------|
| 9/9/2025 | Websocket Data Extraction | Extracts last price, bid, ask, volume data from OKX's public API
| 9/11/2025 | Decision Framework | RTL infrastructure to unpack incoming UART data and make decisions based on it

\
*Planned Features* 
| Feature | Description |
|--------|-------------|
| TBD | TBD |

