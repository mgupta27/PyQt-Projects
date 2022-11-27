import QtQuick 2.0
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4
import QtQuick.Extras.Private 1.0

Rectangle {
    width: 500
    height: 500

    CircularGauge {
        objectName: "motor_gauge"
        property real gauge_value: 0.0
        anchors.centerIn: parent
        value: gauge_value
        maximumValue: 100.0  // Largest Value
        minimumValue: 0.0       // Smallest Value
        style: CircularGaugeStyle {
            id: style
            tickmarkStepSize: 10.0 // Tick Marks

            tickmark: Rectangle {
                visible: styleData.value < 8000 || styleData.value % 1000 == 0
                implicitWidth: outerRadius * 0.02
                antialiasing: true
                implicitHeight: outerRadius * 0.06
                color: styleData.value >= 8000 ? "#ff0000" : "#ff0000"
            }

           minorTickmark: Rectangle {
                visible: styleData.value < 8000
                implicitWidth: outerRadius * 0.01
                antialiasing: true
                implicitHeight: outerRadius * 0.03
                color: "#ff0000"
           }

           tickmarkLabel:  Text {
                font.pixelSize: Math.max(6, outerRadius * 0.1)
                text: styleData.value
                color: styleData.value >= 8000 ? "#ff0000" : "#ff0000"
                antialiasing: true
           }

           needle: Rectangle {
                y: outerRadius * 0.15
                implicitWidth: outerRadius * 0.03
                implicitHeight: outerRadius * 1.1
                antialiasing: true
                color: "#ff0000"
           }
      }
 }
}