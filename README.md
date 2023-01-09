# Read Me - Projekt "Tat oder Wahrheit"

>## Betrieb
>* #### Warum dieses Projekt 
>* #### Welches Problem löst das Projekt 
>* #### Was macht das Projekt
>## Benutzung
>* #### Wie wird das Projekt benutzt
>* #### Welche Optionen oder auch Spezialitäten existieren
>## Architektur
>* #### Kurze Beschreibung des Ablaufs des Programms auf Code Ebene
>## Ungelöste/unbearbeitete Probleme
>* #### Was wurde nicht gelöst?
>* #### Welche Verbesserungen könnten noch gemacht werden?


## Betrieb
#### Warum dieses Projekt
Zu Beginn dieses Projekts wusste ich, dass ich ein Programm im Zusammenhang
mit einem Gemeinschaftsspiel umsetzten möchte. Die erste Idee war,
einen Jass- bzw. Kartenspielrechner zu programmieren. Bei diesem sollte 
der Spielname, die Mitspieler und deren Punkte eingetragen werden können. Da
ich jedoch die Struktur im Hintergrund für dieses Projektes nicht umsetzen konnte
und die Zeit immer knapper wurde, entschied ich mich dazu, ein neues 
Projekt zu starten. Und so entstand die Idee des Spieles 
"Tat oder Wahrheit". Ein Spiel, das viele kennen, einfach zu 
bedienen ist und trotzdem immer wieder Spass bereitet.
<br>
<br>


#### Welches Problem löst das Projekt?
Dieses Projekt und das damit verbundene Programm löst nicht explizit
ein vorhandenes Problem. Es ist mehr eine Möglichkeit, das Spiel auf
einfache Art und Weise zu spielen. Der Aufbau und das Interface
wurde so gestaltet, damit bei einer passenden Gruppe das Spiel möglichst
schnell gestartet werden kann. Zudem sind bereits einige Fragen
und Taten vorhanden, damit man sich selbst nicht allzu viele Gedanken
dazu machen muss.

Mein "Tat oder Wahrheit"-Spiel bietet die Funktion, und dadurch 
einen bedeutenden Mehrwert, dass man selbst weitere Taten und
Wahrheiten hinzufügen kann. Dadurch kann man das Spiel auch in Zukunft
spannend gestalten und stets mit aktuellen Fragen und Aufgaben weiterentwickeln.
<br>
<br>


## Benutzung
#### Wie wird das Projekt benutzt
Die Benutzung dieses Programms ist sehr simpel gehalten. Man hat gleich
zu Beginn die Möglichkeit auszuwählen, ob man ein neues Spiel beginnen
möchte, oder ob man die Taten und Wahrheiten einsehen und gelegentlich
eine neue Fragestellung oder Aufgabe hinzufügen möchte. Stellt man sich
nun also vor, dass man in einer gemütlichen Gruppe beisammen ein Spiel
spielen möchte, ist man nur wenige Klicks davon entfernt. Nach der Auswahl,
dass man ein neues Spiel beginnen möchte, kann man gleich die Entscheidung
treffen, ob die erste Frage eine Tat oder eine Wahrheit sein sollte.
Anschliessend wird gleich die erste Frage oder Aufgabe angezeigt. Sobald diese beantwortet
oder erledigt wurde, kann man erneut auswählen, was als nächstes kommt, Tat oder
Wahrheit. Und so geht das Spiel immer weiter. 
<br>
<br>

#### Welche Optionen oder auch Spezialitäten existieren
Das Einzigartige an diesem Programm ist, dass man selbstständig neue, eigene
Aufgaben oder Fragen hinzufügen kann, welche dann automatisch in das
Spiel eingeschlossen werden. Die Fragen oder Aufgaben kommen mit einer
randon-Funktion, sprich, sie werden willkürlich ausgewählt. Somit weiss
man nie, welche Aufgabe oder Frage als nächstes kommt und ob es vielleicht
sogar eine eigene, hinzugefügte ist. 

Des weiteren verfügt das Programm über eine Funktion, über welche man erkennen kan, ob die neue Tat oder Wahrheit,
welche man selbst hinzugefügt hat, bereits vorhanden ist. Sollte im Tab "Datenbank" der Balken bis zur Nummer 2 gelangen,
so ist diese Tat oder Wahrheit doppelt vorhanden.
<br>
<br>


## Architektur
#### Kurze Beschreibung des Ablaufs des Programms auf Code Ebene
Der Aufbau für dieses Spiel ist folgendermassen:<br>
Es bestehen zwei Listen. Eine mit Taten, eine andere Liste mit Wahrheitsfragen.
Sobald man das Spiel startet und die gewünschte Art (Aufgabe oder Wahrheit) auswählt, ist
der Button mit einer neuen Seite verlinkt. Diese neue Seite hat im Hintergrund
die spezifische Liste verknüpft. Durch eine .random()-Funktion wird jeweils ein immer
anderer Inhalt aus der Liste angezeigt. Dies hat zu Folge, dass der Ablauf der
Taten- oder Wahrheitsausgabe nie derselbe ist. Das führt zu mehr Spannung und
Abwechslung.

Die weitere Funktion des Hinzufügens von Aufgaben oder Wahrheiten ist auf
anderen Seiten geregelt. In dem dazu vorhanden Formular kann man die gewünschte,
neue Tat oder Wahrheit hinzufügen, welche dann der dafür vorgesehenen Liste
als neuer Punkt in einem neuen Absatz hinzugefügt wird.

Durch eine weitere Funktion werden unter dem Formular für die Eingabe
neuer Taten oder Wahrheiten sämtliche Inhalte aus der Liste angezeigt,
sodass man immer sehen kann, welche Taten oder Wahrheiten bereits
vorhanden sind. Die Liste wurde absichtlich in umgekehrter Reihenfolge
angezeigt, damit man bei Eingabe einer eigenen Liste den neuen Inhalt
zuoberst angezeigt erhält. 

Im Abschnitt Datenbank kann man zusätzlich kontrollieren, ob gewisse Taten oder Wahrheiten doppelt vorhanden sind.
Dies funktioniert indem die Liste überprüft, ob ein Inhalt doppelt vorkommt und dies entsprechend ausgibt. 
<br>
<br>

## Ungelöste/unbearbeitete Probleme
#### Was wurde nicht gelöst?
Ein Punkt, welcher nicht gelöst werden konnte, ist, dass man Inhalt
aus der Liste mithilfe eines Buttons o.ä. wieder aus der Liste entfernen
kann. Diese hätte der Vorteil, dass man falsch eingegebene oder bereits vorhandene
Taten und Wahrheiten wieder löschen könnte. 

Der weiteren wäre es spannend, Spieler mit Namen hinzuzufügen und diesen
Punkte für die erledigten Taten und Wahrheiten zu verteilen. Hier war jedoch
das Problem, dass ich diese Struktur, wie bereits beim Jass- oder
Kartenspielrechner gewünscht, nicht erstellen und somit nicht umgesetzt werden
konnte. 
<br>
<br>

#### Welche Verbesserungen könnten noch gemacht werden?
Im Spiel ist beim Wechsel von Taten zu Wahrheiten oder
andersrum eine kurze Verzögerung vorhanden, da diese neue Seite und somit
die andere Liste geladen werden muss. Dieser Fehler könnte evtl. durch
den Einsatz eines Dict oder die Implementierung von unterschiedlichen Listen
auf der gleichen Seite behoben werden. 
