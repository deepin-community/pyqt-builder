# Copyright (c) 2021, Riverbank Computing Limited
# All rights reserved.
#
# This copy of PyQt-builder is licensed for use under the terms of the SIP
# License Agreement.  See the file LICENSE for more details.
#
# This copy of PyQt-builder may also used under the terms of the GNU General
# Public License v2 or v3 as published by the Free Software Foundation which
# can be found in the files LICENSE-GPL2 and LICENSE-GPL3 included in this
# package.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


from ..abstract_package import AbstractPackage
from ..qt_metadata import VersionedMetadata


# The Qt meta-data for this package.
_QT_METADATA = {
    'QtWebEngineCore':
        VersionedMetadata(version=(6, 2, 0),
            other_lib_deps={
                'macos': ('QtWebEngineCore.framework/Helpers/QtWebEngineProcess.app/Contents/Info.plist', )},
            exes={
                'linux': ('libexec/QtWebEngineProcess', ),
                'macos': ('lib/QtWebEngineCore.framework/Helpers/QtWebEngineProcess.app/Contents/MacOS/QtWebEngineProcess', ),
                'win':   ('bin\\QtWebEngineProcess.exe', )},
            files={
                'win':  (('lib\\Qt6Core.lib',
                        "Enable QtWebEngineProcess to find it's resources.\n"), )},
            others={
                'linux': ('resources', 'translations/qtwebengine_locales'),
                'win':   ('resources', 'translations\\qtwebengine_locales')}),

    'QtWebEngineQuick':
        VersionedMetadata(version=(6, 2, 0),
            lib_deps={'': ('QtWebEngineQuickDelegatesQml', )},
            qml=True, qml_names=['QtWebEngine']),

    'QtWebEngineWidgets':
        VersionedMetadata(version=(6, 2, 0)),
}


class PyQt6_WebEngine(AbstractPackage):
    """ The PyQt6-WebEngine package. """

    def get_qt_metadata(self):
        """ Return the package-specific meta-data describing the parts of Qt to
        install.
        """

        return _QT_METADATA
