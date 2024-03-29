import urllib.request as urlreq

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QTabWidget, QVBoxLayout, QLabel, QGroupBox, QGridLayout, \
    QLineEdit, QPushButton, QProgressBar, QComboBox

import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YouTube Downloader")
        self.setMaximumSize(500, 500)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)  # Displaying Max and Min Buttons

        hbox = QHBoxLayout()
        tab_widget = QTabWidget()
        tab_widget.addTab(Download(), "Download")
        tab_widget.addTab(Downloaded(), "Downloaded")

        hbox.addWidget(tab_widget)
        self.setLayout(hbox)
        self.show()


class Download(QWidget):
    def __init__(self):
        super().__init__()

        self.create_layout()
        self.show()

    def create_layout(self):

        layout = QGridLayout()
        self.setLayout(layout)

        groupbox = QGroupBox("Download Videos")
        layout.addWidget(groupbox)

        self.vbox = QVBoxLayout()

        # LINK LABEL AND GET VIDEO BUTTON
        hbox = QHBoxLayout()

        link_label = QLabel(self)
        link_label.setText("Link :")
        hbox.addWidget(link_label)
        line = QLineEdit(self)

        hbox.addWidget(line)

        get_video_button = QPushButton('Get Video', self)
        get_video_button.clicked.connect(self.get_video_button_clicked)
        hbox.addWidget(get_video_button)

        self.vbox.addLayout(hbox)

        groupbox.setLayout(self.vbox)

    def show_download_options(self):

        # THUMBNAILS AND DETAILS ALONG WITH CHECKBOX FOR CHOICES
        thmbnail_vbox = QVBoxLayout()

        # Showing the thumbnail image
        thmbnail_hbox = QHBoxLayout()
        thmbnail_label = QLabel(self)
        # thmbnail_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # start
        url = 'https://i.ytimg.com/vi/XGGWhOUYObc/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBFhhqfIeCHdWELLCJFV5bKyck_Sg'
        data = urlreq.urlopen(url).read()

        image = QtGui.QImage()
        image.loadFromData(data)

        pixmap = QPixmap(image)
        thmbnail_label.setPixmap(pixmap)

        thmbnail_hbox.addWidget(thmbnail_label)

        # Showing the ComboBox for various options
        combo_vbox = QVBoxLayout()

        # Combo Box for Format
        combo_hbox = QHBoxLayout()

        format_label = QLabel()
        format_label.setText("Format :")
        format_label.setAlignment(Qt.AlignRight)
        combo_hbox.addWidget(format_label)

        self.combo = QComboBox()
        self.combo.addItem("Mp3")
        self.combo.addItem("Mp4")
        combo_hbox.addWidget(self.combo)

        combo_vbox.addLayout(combo_hbox)

        # Combo Box for Quality
        combo_hbox = QHBoxLayout()

        format_label = QLabel()
        format_label.setText("Quality :")
        format_label.setAlignment(Qt.AlignRight)
        combo_hbox.addWidget(format_label)

        self.combo = QComboBox()
        self.combo.addItem("1080p")
        self.combo.addItem("720p")
        combo_hbox.addWidget(self.combo)

        combo_vbox.addLayout(combo_hbox)
        thmbnail_hbox.addLayout(combo_vbox)
        thmbnail_vbox.addLayout(thmbnail_hbox)
        self.vbox.addLayout(thmbnail_vbox)

        # PROGRESS BAR AND DOWNLOAD BUTTON
        hbox3 = QHBoxLayout()
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximum(100)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setStyleSheet("QProgressBar {border: 2px solid grey}")
        hbox3.addWidget(self.progress_bar)

        download_button = QPushButton('Download', self)
        download_button.setIcon(QtGui.QIcon("download.png"))
        download_button.clicked.connect(self.download_button_clicked)
        hbox3.addWidget(download_button)

        self.vbox.addLayout(hbox3)

    def get_video_button_clicked(self):
        self.show_download_options()
        # sys.exit()

    def download_button_clicked(self):
        sys.exit()


class Downloaded(QWidget):
    pass


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    App.exec()
