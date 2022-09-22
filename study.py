#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on September 19, 2022, at 16:01
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.4'
expName = 'study'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\study\\study\\study.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "setup"
setupClock = core.Clock()
prompts = [
    "I think that what happened was funny.",
    "I definitely wouldn’t have fallen for that prank.",
    "I feel bad for the target of the prank.",
    "I wish I could have been there to see that!",
    "The target just needs to move on – why do they need to tell the world about it?!",
    "I think that the prank went WAY too far.",
]
pranks = [
    "\"Today my girlfriend decided it would be hilarious if she pulled a prank on me, so she did the classic ‘bucket of water on a door’ one. I ended up getting stitches and a concussion on my birthday.\" (3 July 2012)",
    "\"Today, my friends got me a cake for my birthday. As I blew out the candles, they shoved my head into it and I was knocked out for 3 minutes before an ambulance took me to the hospital. I got a concussion from a cake.\" (8 September 2017)",
    "\"Today, my friends decided to pull a prank. They told my girlfriend I had cheated on her, which I hadn’t. Her revenge? Inviting me over to have me walk in on her with my brother. Our 6-month anniversary was two days away and I got her a trip to Spain, which cost me almost three paychecks.\" (19 December 2018)",
    "\"Today, while I was sleeping, my girlfriend took my phone and set the ringtone to a blood-curdling scream. I found this out when I received a call while driving to work and, thinking someone was being murdered in my backseat, I panicked and swerved into a parked car.\" (1 June 2011)",
    "\"Today, my sister called me at work and told me our elderly mom had passed away. I dropped everything and rushed home, to find out she was fine, and that my sister was just pranking me. When I explained this to my boss, he accused me of lying to get out of work, and I was fired.\" (6 July 2021)"
]

randomInt = randint(1,4)
primer = "error primer"
prankIndex = 0
promptIndex = 0
buttonTEST = visual.ButtonStim(win, 
    text='Click here', font='Arvo',
    pos=(0, 0),
    letterHeight=0.05,
    size=None, borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='buttonTEST'
)
buttonTEST.buttonClock = core.Clock()

# Initialize components for Routine "informationletter"
informationletterClock = core.Clock()
infoLetterContinue = visual.ButtonStim(win, 
    text='Continue', font='Arvo',
    pos=(0.95, -0.95),units='norm',
    letterHeight=0.05,
    size=(0.15, 0.1), borderWidth=0.1,
    fillColor='darkgrey', borderColor=[-1.0000, -1.0000, -1.0000],
    color='white', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='bottom-right',
    name='infoLetterContinue'
)
infoLetterContinue.buttonClock = core.Clock()
win.allowStencil = True
infoletter = visual.Form(win=win, name='infoletter',
    items='informationletter.csv',
    textHeight=0.03,
    font='Open Sans',
    randomize=False,
    style='dark',
    fillColor=None, borderColor=None, itemColor='white', 
    responseColor='white', markerColor='red', colorSpace='rgb', 
    size=(1, 0.8),
    pos=(0, 0),
    itemPadding=0.05
)

# Initialize components for Routine "consent"
consentClock = core.Clock()
consentBtn = visual.ButtonStim(win, 
    text='Continue', font='Arvo',
    pos=(0.95, -0.95),units='norm',
    letterHeight=0.05,
    size=(0.15, 0.1), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='bottom-right',
    name='consentBtn'
)
consentBtn.buttonClock = core.Clock()
win.allowStencil = True
consentform = visual.Form(win=win, name='consentform',
    items='consentform.csv',
    textHeight=0.03,
    font='Open Sans',
    randomize=False,
    style='dark',
    fillColor=None, borderColor=None, itemColor='white', 
    responseColor='white', markerColor='red', colorSpace='rgb', 
    size=(1, 0.8),
    pos=(0, 0),
    itemPadding=0.05
)

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructionsBtn = visual.ButtonStim(win, 
    text='Continue', font='Arvo',
    pos=(0.95, -0.95),units='norm',
    letterHeight=0.05,
    size=(0.15, 0.1), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='bottom-right',
    name='instructionsBtn'
)
instructionsBtn.buttonClock = core.Clock()
win.allowStencil = True
instructionsform = visual.Form(win=win, name='instructionsform',
    items='HO.csv',
    textHeight=0.03,
    font='Open Sans',
    randomize=False,
    style='dark',
    fillColor=None, borderColor=None, itemColor='white', 
    responseColor='white', markerColor='red', colorSpace='rgb', 
    size=(1, 0.8),
    pos=(0, 0),
    itemPadding=0.05
)

# Initialize components for Routine "number"
numberClock = core.Clock()
prankNumberText = visual.TextStim(win=win, name='prankNumberText',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "answer"
answerClock = core.Clock()
prankText = visual.TextStim(win=win, name='prankText',
    text='',
    font='Open Sans',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
promptText = visual.TextStim(win=win, name='promptText',
    text='',
    font='Open Sans',
    pos=(0, -0.11), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
hiddenobserver = visual.TextStim(win=win, name='hiddenobserver',
    text='My "hidden observer" says that:',
    font='Open Sans',
    pos=(0, -0.05), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(1.0, 0.07), pos=(0, -0.3), units=None,
    labels=("Strongly Disagree","","","","","","","Strongly Agree"), ticks=(1, 2, 3, 4, 5, 6, 7, 8), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=True, ori=0.0, depth=-3, readOnly=False)
primertext = visual.TextStim(win=win, name='primertext',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.2098, 0.2098, 0.2059], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "incrementPrompt"
incrementPromptClock = core.Clock()

# Initialize components for Routine "incrementPrank"
incrementPrankClock = core.Clock()

# Initialize components for Routine "respectroutine"
respectroutineClock = core.Clock()
win.allowStencil = True
respectform = visual.Form(win=win, name='respectform',
    items='aboutrespect_part1.csv',
    textHeight=0.03,
    font='Open Sans',
    randomize=False,
    style='dark',
    fillColor=None, borderColor=None, itemColor='white', 
    responseColor='white', markerColor='red', colorSpace='rgb', 
    size=(1, 0.8),
    pos=(0, 0),
    itemPadding=0.05
)
contBtnRespect = visual.ButtonStim(win, 
    text='Continue', font='Arvo',
    pos=(0.95, -0.95),units='norm',
    letterHeight=0.05,
    size=(0.15, 0.1), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='bottom-right',
    name='contBtnRespect'
)
contBtnRespect.buttonClock = core.Clock()

# Initialize components for Routine "angerroutine"
angerroutineClock = core.Clock()
contBtnAnger = visual.ButtonStim(win, 
    text='Continue', font='Arvo',
    pos=(0.95, -0.95),units='norm',
    letterHeight=0.05,
    size=(0.15, 0.1), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='bottom-right',
    name='contBtnAnger'
)
contBtnAnger.buttonClock = core.Clock()
win.allowStencil = True
angerform = visual.Form(win=win, name='angerform',
    items='aboutanger - Sheet1.csv',
    textHeight=0.03,
    font='Open Sans',
    randomize=False,
    style='dark',
    fillColor=None, borderColor=None, itemColor='white', 
    responseColor='white', markerColor='red', colorSpace='rgb', 
    size=(1, 0.8),
    pos=(0, 0),
    itemPadding=0.05
)

# Initialize components for Routine "demoroutine"
demoroutineClock = core.Clock()
win.allowStencil = True
demoForm = visual.Form(win=win, name='demoForm',
    items='demographic.csv',
    textHeight=0.03,
    font='Open Sans',
    randomize=False,
    style='dark',
    fillColor=None, borderColor=None, itemColor='white', 
    responseColor='white', markerColor='red', colorSpace='rgb', 
    size=(1, 0.8),
    pos=(0, 0),
    itemPadding=0.05
)
contBtnDemo = visual.ButtonStim(win, 
    text='Continue', font='Arvo',
    pos=(0.95, -0.95),units='norm',
    letterHeight=0.05,
    size=(0.15, 0.1), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='bottom-right',
    name='contBtnDemo'
)
contBtnDemo.buttonClock = core.Clock()

# Initialize components for Routine "finish"
finishClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Study Complete',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedbackBtn = visual.ButtonStim(win, 
    text='Continue', font='Arvo',
    pos=(0.95, -0.95),units='norm',
    letterHeight=0.05,
    size=(0.15, 0.1), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='bottom-right',
    name='feedbackBtn'
)
feedbackBtn.buttonClock = core.Clock()
win.allowStencil = True
feedbackform = visual.Form(win=win, name='feedbackform',
    items='feedbackletter.csv',
    textHeight=0.03,
    font='Open Sans',
    randomize=False,
    style='dark',
    fillColor=None, borderColor=None, itemColor='white', 
    responseColor='white', markerColor='red', colorSpace='rgb', 
    size=(1, 0.8),
    pos=(0, 0),
    itemPadding=0.05
)

# Initialize components for Routine "debrief"
debriefClock = core.Clock()
debriefBtn = visual.ButtonStim(win, 
    text='Continue', font='Arvo',
    pos=(0.95, -0.95),units='norm',
    letterHeight=0.05,
    size=(0.15, 0.1), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='bottom-right',
    name='debriefBtn'
)
debriefBtn.buttonClock = core.Clock()
win.allowStencil = True
debriefform = visual.Form(win=win, name='debriefform',
    items='debriefform.csv',
    textHeight=0.03,
    font='Open Sans',
    randomize=False,
    style='dark',
    fillColor=None, borderColor=None, itemColor='white', 
    responseColor='white', markerColor='red', colorSpace='rgb', 
    size=(1, 0.8),
    pos=(0, 0),
    itemPadding=0.05
)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
setupComponents = [buttonTEST]
for thisComponent in setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setup"-------
while continueRoutine:
    # get current time
    t = setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *buttonTEST* updates
    if buttonTEST.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        buttonTEST.frameNStart = frameN  # exact frame index
        buttonTEST.tStart = t  # local t and not account for scr refresh
        buttonTEST.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttonTEST, 'tStartRefresh')  # time at next scr refresh
        buttonTEST.setAutoDraw(True)
    if buttonTEST.status == STARTED:
        # check whether buttonTEST has been pressed
        if buttonTEST.isClicked:
            if not buttonTEST.wasClicked:
                buttonTEST.timesOn.append(buttonTEST.buttonClock.getTime()) # store time of first click
                buttonTEST.timesOff.append(buttonTEST.buttonClock.getTime()) # store time clicked until
            else:
                buttonTEST.timesOff[-1] = buttonTEST.buttonClock.getTime() # update time clicked until
            if not buttonTEST.wasClicked:
                continueRoutine = False  # end routine when buttonTEST is clicked
                None
            buttonTEST.wasClicked = True  # if buttonTEST is still clicked next frame, it is not a new click
        else:
            buttonTEST.wasClicked = False  # if buttonTEST is clicked next frame, it is a new click
    else:
        buttonTEST.wasClicked = False  # if buttonTEST is clicked next frame, it is a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setup"-------
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if randomInt == 1:
    primer = "You're nothing"
elif randomInt == 2:
    primer = "You're great"
elif randomInt == 3:
    primer = "People are walking"
else:
    primer = "Error 2"
    
thisExp.addData('study.primer', primer)
thisExp.addData('buttonTEST.started', buttonTEST.tStartRefresh)
thisExp.addData('buttonTEST.stopped', buttonTEST.tStopRefresh)
thisExp.addData('buttonTEST.numClicks', buttonTEST.numClicks)
if buttonTEST.numClicks:
   thisExp.addData('buttonTEST.timesOn', buttonTEST.timesOn)
   thisExp.addData('buttonTEST.timesOff', buttonTEST.timesOff)
else:
   thisExp.addData('buttonTEST.timesOn', "")
   thisExp.addData('buttonTEST.timesOff', "")
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "informationletter"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
informationletterComponents = [infoLetterContinue, infoletter]
for thisComponent in informationletterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
informationletterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "informationletter"-------
while continueRoutine:
    # get current time
    t = informationletterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=informationletterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *infoLetterContinue* updates
    if infoLetterContinue.status == NOT_STARTED and frameN >= 0:
        # keep track of start time/frame for later
        infoLetterContinue.frameNStart = frameN  # exact frame index
        infoLetterContinue.tStart = t  # local t and not account for scr refresh
        infoLetterContinue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(infoLetterContinue, 'tStartRefresh')  # time at next scr refresh
        infoLetterContinue.setAutoDraw(True)
    if infoLetterContinue.status == STARTED:
        # check whether infoLetterContinue has been pressed
        if infoLetterContinue.isClicked:
            if not infoLetterContinue.wasClicked:
                infoLetterContinue.timesOn.append(infoLetterContinue.buttonClock.getTime()) # store time of first click
                infoLetterContinue.timesOff.append(infoLetterContinue.buttonClock.getTime()) # store time clicked until
            else:
                infoLetterContinue.timesOff[-1] = infoLetterContinue.buttonClock.getTime() # update time clicked until
            if not infoLetterContinue.wasClicked:
                continueRoutine = False  # end routine when infoLetterContinue is clicked
                None
            infoLetterContinue.wasClicked = True  # if infoLetterContinue is still clicked next frame, it is not a new click
        else:
            infoLetterContinue.wasClicked = False  # if infoLetterContinue is clicked next frame, it is a new click
    else:
        infoLetterContinue.wasClicked = False  # if infoLetterContinue is clicked next frame, it is a new click
    
    # *infoletter* updates
    if infoletter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        infoletter.frameNStart = frameN  # exact frame index
        infoletter.tStart = t  # local t and not account for scr refresh
        infoletter.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(infoletter, 'tStartRefresh')  # time at next scr refresh
        infoletter.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in informationletterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "informationletter"-------
for thisComponent in informationletterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
infoletter.addDataToExp(thisExp, 'rows')
infoletter.autodraw = False
# the Routine "informationletter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "consent"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
consentComponents = [consentBtn, consentform]
for thisComponent in consentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
consentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "consent"-------
while continueRoutine:
    # get current time
    t = consentClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=consentClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *consentBtn* updates
    if consentBtn.status == NOT_STARTED and consentform.complete:
        # keep track of start time/frame for later
        consentBtn.frameNStart = frameN  # exact frame index
        consentBtn.tStart = t  # local t and not account for scr refresh
        consentBtn.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consentBtn, 'tStartRefresh')  # time at next scr refresh
        consentBtn.setAutoDraw(True)
    if consentBtn.status == STARTED:
        # check whether consentBtn has been pressed
        if consentBtn.isClicked:
            if not consentBtn.wasClicked:
                consentBtn.timesOn.append(consentBtn.buttonClock.getTime()) # store time of first click
                consentBtn.timesOff.append(consentBtn.buttonClock.getTime()) # store time clicked until
            else:
                consentBtn.timesOff[-1] = consentBtn.buttonClock.getTime() # update time clicked until
            if not consentBtn.wasClicked:
                continueRoutine = False  # end routine when consentBtn is clicked
                None
            consentBtn.wasClicked = True  # if consentBtn is still clicked next frame, it is not a new click
        else:
            consentBtn.wasClicked = False  # if consentBtn is clicked next frame, it is a new click
    else:
        consentBtn.wasClicked = False  # if consentBtn is clicked next frame, it is a new click
    
    # *consentform* updates
    if consentform.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        consentform.frameNStart = frameN  # exact frame index
        consentform.tStart = t  # local t and not account for scr refresh
        consentform.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consentform, 'tStartRefresh')  # time at next scr refresh
        consentform.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in consentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "consent"-------
for thisComponent in consentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('consentBtn.started', consentBtn.tStartRefresh)
thisExp.addData('consentBtn.stopped', consentBtn.tStopRefresh)
consentform.addDataToExp(thisExp, 'rows')
consentform.autodraw = False
# the Routine "consent" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
instructionsComponents = [instructionsBtn, instructionsform]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructionsBtn* updates
    if instructionsBtn.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        instructionsBtn.frameNStart = frameN  # exact frame index
        instructionsBtn.tStart = t  # local t and not account for scr refresh
        instructionsBtn.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionsBtn, 'tStartRefresh')  # time at next scr refresh
        instructionsBtn.setAutoDraw(True)
    if instructionsBtn.status == STARTED:
        # check whether instructionsBtn has been pressed
        if instructionsBtn.isClicked:
            if not instructionsBtn.wasClicked:
                instructionsBtn.timesOn.append(instructionsBtn.buttonClock.getTime()) # store time of first click
                instructionsBtn.timesOff.append(instructionsBtn.buttonClock.getTime()) # store time clicked until
            else:
                instructionsBtn.timesOff[-1] = instructionsBtn.buttonClock.getTime() # update time clicked until
            if not instructionsBtn.wasClicked:
                continueRoutine = False  # end routine when instructionsBtn is clicked
                None
            instructionsBtn.wasClicked = True  # if instructionsBtn is still clicked next frame, it is not a new click
        else:
            instructionsBtn.wasClicked = False  # if instructionsBtn is clicked next frame, it is a new click
    else:
        instructionsBtn.wasClicked = False  # if instructionsBtn is clicked next frame, it is a new click
    
    # *instructionsform* updates
    if instructionsform.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionsform.frameNStart = frameN  # exact frame index
        instructionsform.tStart = t  # local t and not account for scr refresh
        instructionsform.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionsform, 'tStartRefresh')  # time at next scr refresh
        instructionsform.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructionsBtn.started', instructionsBtn.tStartRefresh)
thisExp.addData('instructionsBtn.stopped', instructionsBtn.tStopRefresh)
thisExp.addData('instructionsBtn.numClicks', instructionsBtn.numClicks)
if instructionsBtn.numClicks:
   thisExp.addData('instructionsBtn.timesOn', instructionsBtn.timesOn)
   thisExp.addData('instructionsBtn.timesOff', instructionsBtn.timesOff)
else:
   thisExp.addData('instructionsBtn.timesOn', "")
   thisExp.addData('instructionsBtn.timesOff', "")
instructionsform.addDataToExp(thisExp, 'rows')
instructionsform.autodraw = False
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pranksLoop = data.TrialHandler(nReps=len(pranks), method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='pranksLoop')
thisExp.addLoop(pranksLoop)  # add the loop to the experiment
thisPranksLoop = pranksLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPranksLoop.rgb)
if thisPranksLoop != None:
    for paramName in thisPranksLoop:
        exec('{} = thisPranksLoop[paramName]'.format(paramName))

for thisPranksLoop in pranksLoop:
    currentLoop = pranksLoop
    # abbreviate parameter names if possible (e.g. rgb = thisPranksLoop.rgb)
    if thisPranksLoop != None:
        for paramName in thisPranksLoop:
            exec('{} = thisPranksLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "number"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    prankNumberText.setText("Prank " + str(prankIndex + 1))
    # keep track of which components have finished
    numberComponents = [prankNumberText]
    for thisComponent in numberComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    numberClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "number"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = numberClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=numberClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prankNumberText* updates
        if prankNumberText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prankNumberText.frameNStart = frameN  # exact frame index
            prankNumberText.tStart = t  # local t and not account for scr refresh
            prankNumberText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prankNumberText, 'tStartRefresh')  # time at next scr refresh
            prankNumberText.setAutoDraw(True)
        if prankNumberText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prankNumberText.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                prankNumberText.tStop = t  # not accounting for scr refresh
                prankNumberText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(prankNumberText, 'tStopRefresh')  # time at next scr refresh
                prankNumberText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in numberComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "number"-------
    for thisComponent in numberComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    promptLoop = data.TrialHandler(nReps=len(prompts), method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='promptLoop')
    thisExp.addLoop(promptLoop)  # add the loop to the experiment
    thisPromptLoop = promptLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPromptLoop.rgb)
    if thisPromptLoop != None:
        for paramName in thisPromptLoop:
            exec('{} = thisPromptLoop[paramName]'.format(paramName))
    
    for thisPromptLoop in promptLoop:
        currentLoop = promptLoop
        # abbreviate parameter names if possible (e.g. rgb = thisPromptLoop.rgb)
        if thisPromptLoop != None:
            for paramName in thisPromptLoop:
                exec('{} = thisPromptLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "answer"-------
        continueRoutine = True
        # update component parameters for each repeat
        slider.reset()
        primertext.setText(primer
)
        prankVar = pranks[prankIndex]
        promptVar = prompts[promptIndex]
        thisExp.addData('prankVar.routineValue', '"' + prankVar)
        thisExp.addData('promptVar.routineValue', '"' + promptVar + '"')
        # keep track of which components have finished
        answerComponents = [prankText, promptText, hiddenobserver, slider, primertext]
        for thisComponent in answerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        answerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "answer"-------
        while continueRoutine:
            # get current time
            t = answerClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=answerClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *prankText* updates
            if prankText.status == NOT_STARTED and frameN >= 2:
                # keep track of start time/frame for later
                prankText.frameNStart = frameN  # exact frame index
                prankText.tStart = t  # local t and not account for scr refresh
                prankText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prankText, 'tStartRefresh')  # time at next scr refresh
                prankText.setAutoDraw(True)
            if prankText.status == STARTED:  # only update if drawing
                prankText.setText(prankVar, log=False)
            
            # *promptText* updates
            if promptText.status == NOT_STARTED and frameN >= 2:
                # keep track of start time/frame for later
                promptText.frameNStart = frameN  # exact frame index
                promptText.tStart = t  # local t and not account for scr refresh
                promptText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(promptText, 'tStartRefresh')  # time at next scr refresh
                promptText.setAutoDraw(True)
            if promptText.status == STARTED:  # only update if drawing
                promptText.setText(promptVar, log=False)
            
            # *hiddenobserver* updates
            if hiddenobserver.status == NOT_STARTED and frameN >= 2:
                # keep track of start time/frame for later
                hiddenobserver.frameNStart = frameN  # exact frame index
                hiddenobserver.tStart = t  # local t and not account for scr refresh
                hiddenobserver.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hiddenobserver, 'tStartRefresh')  # time at next scr refresh
                hiddenobserver.setAutoDraw(True)
            
            # *slider* updates
            if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider.frameNStart = frameN  # exact frame index
                slider.tStart = t  # local t and not account for scr refresh
                slider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
                slider.setAutoDraw(True)
            
            # Check slider for response to end routine
            if slider.getRating() is not None and slider.status == STARTED:
                continueRoutine = False
            
            # *primertext* updates
            if primertext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                primertext.frameNStart = frameN  # exact frame index
                primertext.tStart = t  # local t and not account for scr refresh
                primertext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(primertext, 'tStartRefresh')  # time at next scr refresh
                primertext.setAutoDraw(True)
            if primertext.status == STARTED:
                if frameN >= 1:
                    # keep track of stop time/frame for later
                    primertext.tStop = t  # not accounting for scr refresh
                    primertext.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(primertext, 'tStopRefresh')  # time at next scr refresh
                    primertext.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in answerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "answer"-------
        for thisComponent in answerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        promptLoop.addData('slider.response', slider.getRating())
        promptLoop.addData('slider.rt', slider.getRT())
        promptLoop.addData('slider.started', slider.tStartRefresh)
        promptLoop.addData('slider.stopped', slider.tStopRefresh)
        # the Routine "answer" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "incrementPrompt"-------
        continueRoutine = True
        # update component parameters for each repeat
        promptIndex = promptIndex + 1
        # keep track of which components have finished
        incrementPromptComponents = []
        for thisComponent in incrementPromptComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        incrementPromptClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "incrementPrompt"-------
        while continueRoutine:
            # get current time
            t = incrementPromptClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=incrementPromptClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in incrementPromptComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "incrementPrompt"-------
        for thisComponent in incrementPromptComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "incrementPrompt" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed len(prompts) repeats of 'promptLoop'
    
    
    # ------Prepare to start Routine "incrementPrank"-------
    continueRoutine = True
    # update component parameters for each repeat
    prankIndex = prankIndex + 1
    promptIndex = 0
    # keep track of which components have finished
    incrementPrankComponents = []
    for thisComponent in incrementPrankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    incrementPrankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "incrementPrank"-------
    while continueRoutine:
        # get current time
        t = incrementPrankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=incrementPrankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in incrementPrankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "incrementPrank"-------
    for thisComponent in incrementPrankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "incrementPrank" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed len(pranks) repeats of 'pranksLoop'


# ------Prepare to start Routine "respectroutine"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
respectroutineComponents = [respectform, contBtnRespect]
for thisComponent in respectroutineComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
respectroutineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "respectroutine"-------
while continueRoutine:
    # get current time
    t = respectroutineClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=respectroutineClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *respectform* updates
    if respectform.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        respectform.frameNStart = frameN  # exact frame index
        respectform.tStart = t  # local t and not account for scr refresh
        respectform.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(respectform, 'tStartRefresh')  # time at next scr refresh
        respectform.setAutoDraw(True)
    
    # *contBtnRespect* updates
    if contBtnRespect.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        contBtnRespect.frameNStart = frameN  # exact frame index
        contBtnRespect.tStart = t  # local t and not account for scr refresh
        contBtnRespect.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(contBtnRespect, 'tStartRefresh')  # time at next scr refresh
        contBtnRespect.setAutoDraw(True)
    if contBtnRespect.status == STARTED:
        # check whether contBtnRespect has been pressed
        if contBtnRespect.isClicked:
            if not contBtnRespect.wasClicked:
                contBtnRespect.timesOn.append(contBtnRespect.buttonClock.getTime()) # store time of first click
                contBtnRespect.timesOff.append(contBtnRespect.buttonClock.getTime()) # store time clicked until
            else:
                contBtnRespect.timesOff[-1] = contBtnRespect.buttonClock.getTime() # update time clicked until
            if not contBtnRespect.wasClicked:
                continueRoutine = False  # end routine when contBtnRespect is clicked
                None
            contBtnRespect.wasClicked = True  # if contBtnRespect is still clicked next frame, it is not a new click
        else:
            contBtnRespect.wasClicked = False  # if contBtnRespect is clicked next frame, it is a new click
    else:
        contBtnRespect.wasClicked = False  # if contBtnRespect is clicked next frame, it is a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in respectroutineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "respectroutine"-------
for thisComponent in respectroutineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
respectform.addDataToExp(thisExp, 'rows')
respectform.autodraw = False
# the Routine "respectroutine" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "angerroutine"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
angerroutineComponents = [contBtnAnger, angerform]
for thisComponent in angerroutineComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
angerroutineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "angerroutine"-------
while continueRoutine:
    # get current time
    t = angerroutineClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=angerroutineClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *contBtnAnger* updates
    if contBtnAnger.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        contBtnAnger.frameNStart = frameN  # exact frame index
        contBtnAnger.tStart = t  # local t and not account for scr refresh
        contBtnAnger.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(contBtnAnger, 'tStartRefresh')  # time at next scr refresh
        contBtnAnger.setAutoDraw(True)
    if contBtnAnger.status == STARTED:
        # check whether contBtnAnger has been pressed
        if contBtnAnger.isClicked:
            if not contBtnAnger.wasClicked:
                contBtnAnger.timesOn.append(contBtnAnger.buttonClock.getTime()) # store time of first click
                contBtnAnger.timesOff.append(contBtnAnger.buttonClock.getTime()) # store time clicked until
            else:
                contBtnAnger.timesOff[-1] = contBtnAnger.buttonClock.getTime() # update time clicked until
            if not contBtnAnger.wasClicked:
                continueRoutine = False  # end routine when contBtnAnger is clicked
                None
            contBtnAnger.wasClicked = True  # if contBtnAnger is still clicked next frame, it is not a new click
        else:
            contBtnAnger.wasClicked = False  # if contBtnAnger is clicked next frame, it is a new click
    else:
        contBtnAnger.wasClicked = False  # if contBtnAnger is clicked next frame, it is a new click
    
    # *angerform* updates
    if angerform.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        angerform.frameNStart = frameN  # exact frame index
        angerform.tStart = t  # local t and not account for scr refresh
        angerform.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(angerform, 'tStartRefresh')  # time at next scr refresh
        angerform.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in angerroutineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "angerroutine"-------
for thisComponent in angerroutineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
angerform.addDataToExp(thisExp, 'rows')
angerform.autodraw = False
# the Routine "angerroutine" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demoroutine"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
demoroutineComponents = [demoForm, contBtnDemo]
for thisComponent in demoroutineComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demoroutineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "demoroutine"-------
while continueRoutine:
    # get current time
    t = demoroutineClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demoroutineClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *demoForm* updates
    if demoForm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoForm.frameNStart = frameN  # exact frame index
        demoForm.tStart = t  # local t and not account for scr refresh
        demoForm.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoForm, 'tStartRefresh')  # time at next scr refresh
        demoForm.setAutoDraw(True)
    
    # *contBtnDemo* updates
    if contBtnDemo.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        contBtnDemo.frameNStart = frameN  # exact frame index
        contBtnDemo.tStart = t  # local t and not account for scr refresh
        contBtnDemo.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(contBtnDemo, 'tStartRefresh')  # time at next scr refresh
        contBtnDemo.setAutoDraw(True)
    if contBtnDemo.status == STARTED:
        # check whether contBtnDemo has been pressed
        if contBtnDemo.isClicked:
            if not contBtnDemo.wasClicked:
                contBtnDemo.timesOn.append(contBtnDemo.buttonClock.getTime()) # store time of first click
                contBtnDemo.timesOff.append(contBtnDemo.buttonClock.getTime()) # store time clicked until
            else:
                contBtnDemo.timesOff[-1] = contBtnDemo.buttonClock.getTime() # update time clicked until
            if not contBtnDemo.wasClicked:
                continueRoutine = False  # end routine when contBtnDemo is clicked
                None
            contBtnDemo.wasClicked = True  # if contBtnDemo is still clicked next frame, it is not a new click
        else:
            contBtnDemo.wasClicked = False  # if contBtnDemo is clicked next frame, it is a new click
    else:
        contBtnDemo.wasClicked = False  # if contBtnDemo is clicked next frame, it is a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demoroutineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demoroutine"-------
for thisComponent in demoroutineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
demoForm.addDataToExp(thisExp, 'rows')
demoForm.autodraw = False
# the Routine "demoroutine" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "finish"-------
continueRoutine = True
routineTimer.add(1.500000)
# update component parameters for each repeat
# keep track of which components have finished
finishComponents = [text_2]
for thisComponent in finishComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
finishClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "finish"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = finishClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=finishClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 1.5-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "finish"-------
for thisComponent in finishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "feedback"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
feedbackComponents = [feedbackBtn, feedbackform]
for thisComponent in feedbackComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "feedback"-------
while continueRoutine:
    # get current time
    t = feedbackClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *feedbackBtn* updates
    if feedbackBtn.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        feedbackBtn.frameNStart = frameN  # exact frame index
        feedbackBtn.tStart = t  # local t and not account for scr refresh
        feedbackBtn.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedbackBtn, 'tStartRefresh')  # time at next scr refresh
        feedbackBtn.setAutoDraw(True)
    if feedbackBtn.status == STARTED:
        # check whether feedbackBtn has been pressed
        if feedbackBtn.isClicked:
            if not feedbackBtn.wasClicked:
                feedbackBtn.timesOn.append(feedbackBtn.buttonClock.getTime()) # store time of first click
                feedbackBtn.timesOff.append(feedbackBtn.buttonClock.getTime()) # store time clicked until
            else:
                feedbackBtn.timesOff[-1] = feedbackBtn.buttonClock.getTime() # update time clicked until
            if not feedbackBtn.wasClicked:
                continueRoutine = False  # end routine when feedbackBtn is clicked
                None
            feedbackBtn.wasClicked = True  # if feedbackBtn is still clicked next frame, it is not a new click
        else:
            feedbackBtn.wasClicked = False  # if feedbackBtn is clicked next frame, it is a new click
    else:
        feedbackBtn.wasClicked = False  # if feedbackBtn is clicked next frame, it is a new click
    
    # *feedbackform* updates
    if feedbackform.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        feedbackform.frameNStart = frameN  # exact frame index
        feedbackform.tStart = t  # local t and not account for scr refresh
        feedbackform.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedbackform, 'tStartRefresh')  # time at next scr refresh
        feedbackform.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "feedback"-------
for thisComponent in feedbackComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('feedbackBtn.numClicks', feedbackBtn.numClicks)
if feedbackBtn.numClicks:
   thisExp.addData('feedbackBtn.timesOn', feedbackBtn.timesOn)
   thisExp.addData('feedbackBtn.timesOff', feedbackBtn.timesOff)
else:
   thisExp.addData('feedbackBtn.timesOn', "")
   thisExp.addData('feedbackBtn.timesOff', "")
feedbackform.addDataToExp(thisExp, 'rows')
feedbackform.autodraw = False
# the Routine "feedback" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "debrief"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
debriefComponents = [debriefBtn, debriefform]
for thisComponent in debriefComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
debriefClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "debrief"-------
while continueRoutine:
    # get current time
    t = debriefClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=debriefClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *debriefBtn* updates
    if debriefBtn.status == NOT_STARTED and debriefform.complete:
        # keep track of start time/frame for later
        debriefBtn.frameNStart = frameN  # exact frame index
        debriefBtn.tStart = t  # local t and not account for scr refresh
        debriefBtn.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(debriefBtn, 'tStartRefresh')  # time at next scr refresh
        debriefBtn.setAutoDraw(True)
    if debriefBtn.status == STARTED:
        # check whether debriefBtn has been pressed
        if debriefBtn.isClicked:
            if not debriefBtn.wasClicked:
                debriefBtn.timesOn.append(debriefBtn.buttonClock.getTime()) # store time of first click
                debriefBtn.timesOff.append(debriefBtn.buttonClock.getTime()) # store time clicked until
            else:
                debriefBtn.timesOff[-1] = debriefBtn.buttonClock.getTime() # update time clicked until
            if not debriefBtn.wasClicked:
                continueRoutine = False  # end routine when debriefBtn is clicked
                None
            debriefBtn.wasClicked = True  # if debriefBtn is still clicked next frame, it is not a new click
        else:
            debriefBtn.wasClicked = False  # if debriefBtn is clicked next frame, it is a new click
    else:
        debriefBtn.wasClicked = False  # if debriefBtn is clicked next frame, it is a new click
    
    # *debriefform* updates
    if debriefform.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        debriefform.frameNStart = frameN  # exact frame index
        debriefform.tStart = t  # local t and not account for scr refresh
        debriefform.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(debriefform, 'tStartRefresh')  # time at next scr refresh
        debriefform.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in debriefComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "debrief"-------
for thisComponent in debriefComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('debriefBtn.numClicks', debriefBtn.numClicks)
if debriefBtn.numClicks:
   thisExp.addData('debriefBtn.timesOn', debriefBtn.timesOn)
   thisExp.addData('debriefBtn.timesOff', debriefBtn.timesOff)
else:
   thisExp.addData('debriefBtn.timesOn', "")
   thisExp.addData('debriefBtn.timesOff', "")
debriefform.addDataToExp(thisExp, 'rows')
debriefform.autodraw = False
# the Routine "debrief" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
