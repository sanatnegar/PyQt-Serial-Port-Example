from Ui_Dialog import *
from PyQt5.QtCore import qDebug, QIODevice
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo


class Dialog(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.serialPort = QSerialPort()
        self.cmbPorts.addItems([serialPort.portName() for serialPort in QSerialPortInfo().availablePorts()])
        self.handle_controls()
        self.serialDeviceIsConnectedFlag = False
        self.serialPort.readyRead.connect(self.on_serial_data_available)
        self.buffer = ""
        self.lePwm.setText("0")

    def handle_controls(self):
        self.btnConnect.clicked.connect(self.open_serial_port)
        self.btnDisconnect.clicked.connect(self.close_serial_port)
        self.sldPWM.valueChanged.connect(self.update_pwm_value)
        self.btnUpdatePwm.clicked.connect(self.send_pwm)

    def open_serial_port(self):
        if not self.serialDeviceIsConnectedFlag:
            self.serialPort.setPortName(self.cmbPorts.currentText())
            qDebug("Connecting to: " + self.serialPort.portName())
            if self.serialPort.open(QIODevice.ReadWrite):

                if not self.serialPort.setBaudRate(QSerialPort.BaudRate.Baud115200):
                    qDebug(self.serialPort.errorString())

                if not self.serialPort.setDataBits(QSerialPort.DataBits.Data8):
                    qDebug(self.serialPort.errorString())

                if not self.serialPort.setParity(QSerialPort.Parity.NoParity):
                    qDebug(self.serialPort.errorString())

                if not self.serialPort.setFlowControl(QSerialPort.FlowControl.NoFlowControl):
                    qDebug(self.serialPort.errorString())

                qDebug(self.serialPort.portName() + " connected")
                self.serialDeviceIsConnectedFlag = True
                self.btnConnect.setEnabled(False)
                self.btnDisconnect.setEnabled(True)
                self.cmbPorts.setEnabled(False)

            else:
                qDebug(self.serialPort.portName() + " not connected")
                qDebug("Error: " + self.serialPort.errorString())
                self.serialDeviceIsConnectedFlag = False
                self.btnConnect.setEnabled(True)
                self.btnDisconnect.setEnabled(False)

        else:
            qDebug("Error: Can not connect, another device is connected")

    def close_serial_port(self):
        if self.serialDeviceIsConnectedFlag:
            self.serialPort.close();
            self.serialDeviceIsConnectedFlag = False
            qDebug("Connection Closed")
            self.btnConnect.setEnabled(True)
            self.btnDisconnect.setEnabled(False)
            self.cmbPorts.setEnabled(True)

        else:
            qDebug("Error: Can not disconnect, no device is connected")

    def update_pwm_value(self):
        self.lePwm.setText(str(self.sldPWM.value()))

    def send_pwm(self):
        self.serial_write(self.lePwm.text())

    def on_serial_data_available(self):
        if self.serialDeviceIsConnectedFlag:
            try:
                self.buffer += str(self.serialPort.readAll(), 'utf-8')
                start_sign_position = self.buffer.find("#")
                end_sign_pos = self.buffer.find("|", start_sign_position)

                if "#" in self.buffer and "|" in self.buffer and start_sign_position < end_sign_pos:
                    self.update_ui(self.buffer)
                    self.buffer = ""
                    self.serialPort.flush()
            except:
                qDebug("Error: Uncompleted Packet Ignored")

    def update_ui(self, buffer):
        start = buffer.find("#")
        end = buffer.find("|", start)
        clean = buffer[start:end]
        data = clean.split(",")

        try:
            self.pbAI_0.setValue(int(data[0][1:]))  # removing '#' sign
            self.pbAI_1.setValue(int(data[1]))
            self.pbAI_2.setValue(int(data[2]))
            self.pbAI_3.setValue(int(data[3]))
            self.pbAI_4.setValue(int(data[4]))
            self.pbAI_5.setValue(int(data[5]))

            self.leAI_0.setText(str(data[0][1:]))
            self.leAI_1.setText(str(data[1]))
            self.leAI_2.setText(str(data[2]))
            self.leAI_3.setText(str(data[3]))
            self.leAI_4.setText(str(data[4]))
            self.leAI_5.setText(str(data[5]))

        except:
            pass

    def serial_write(self, packet):
        if self.serialDeviceIsConnectedFlag:
            packet = packet + '\n'
            self.serialPort.write(packet.encode())
