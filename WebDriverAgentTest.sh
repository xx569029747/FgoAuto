#! /bin/bash

cd /Volumes/EveryThing/Documents/Workspace/WebDriverAgent/

UDID=$(idevice_id -l | head -n1)

nohup /Volumes/EveryThing/Applications/Xcode-beta.app/Contents/Developer/usr/bin/xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination "id=$UDID" test >> ~/Downloads/webDriverAgebt.out &

nohup iproxy 8100 8100 >> iproxy.out &
