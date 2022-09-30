#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on September 30, 2022, at 18:12
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
    originPath='C:\\study\\study\\study_lastrun.py',
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

# Initialize components for Routine "informationletter"
informationletterClock = core.Clock()
win.allowStencil = True
infoletter = visual.Form(win=win, name='infoletter',
    items='informationletter.csv',
    textHeight=0.03,
    font='Open Sans',
    randomize=False,
    style='dark',
    fillColor=None, borderColor=None, itemColor='white', 
    responseColor='white', markerColor='red', colorSpace='rgb', 
    size=(1.5, 0.8),
    pos=(0, 0),
    itemPadding=0.05
)
infoContinuePrompt = visual.TextStim(win=win, name='infoContinuePrompt',
    text='Press Space to Submit and Continue',
    font='Open Sans',
    pos=(0, -0.45), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
infoKey = keyboard.Keyboard()

# Initialize components for Routine "consent"
consentClock = core.Clock()
win.allowStencil = True
consentform = visual.Form(win=win, name='consentform',
    items='consentform.csv',
    textHeight=0.03,
    font='Open Sans',
    randomize=False,
    style='dark',
    fillColor=None, borderColor=None, itemColor='white', 
    responseColor='white', markerColor='red', colorSpace='rgb', 
    size=(1.5, 0.8),
    pos=(0, 0),
    itemPadding=0.05
)
consentContinuePrompt = visual.TextStim(win=win, name='consentContinuePrompt',
    text='Press Space to Submit and Continue',
    font='Open Sans',
    pos=(0, -0.45), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
consentKey = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
win.allowStencil = True
instructionsform = visual.Form(win=win, name='instructionsform',
    items='HO.csv',
    textHeight=0.03,
    font='Open Sans',
    randomize=False,
    style='dark',
    fillColor=None, borderColor=None, itemColor='white', 
    responseColor='white', markerColor='red', colorSpace='rgb', 
    size=(1.5, 0.8),
    pos=(0, 0),
    itemPadding=0.05
)
instructContinuePrompt = visual.TextStim(win=win, name='instructContinuePrompt',
    text='Press Space to Submit and Continue',
    font='Open Sans',
    pos=(0, -0.45), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instructKey = keyboard.Keyboard()

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
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
answerContinuePrompt = visual.TextStim(win=win, name='answerContinuePrompt',
    text='Press Space to Submit and Continue',
    font='Open Sans',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
answerKey = keyboard.Keyboard()

# Initialize components for Routine "incrementPrompt"
incrementPromptClock = core.Clock()

# Initialize components for Routine "incrementPrank"
incrementPrankClock = core.Clock()

# Initialize components for Routine "respectroutine"
respectroutineClock = core.Clock()
win.allowStencil = True
respectform = visual.Form(win=win, name='respectform',
    items='aboutrespect.csv',
    textHeight=0.03,
    font='Open Sans',
    randomize=False,
    style='dark',
    fillColor=None, borderColor=None, itemColor='white', 
    responseColor='white', markerColor='red', colorSpace='rgb', 
    size=(1.5, 0.8),
    pos=(0, 0),
    itemPadding=0.05
)
respectContinuePrompt = visual.TextStim(win=win, name='respectContinuePrompt',
    text='Press Space to Submit and Continue',
    font='Open Sans',
    pos=(0, -0.45), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
respectKey = keyboard.Keyboard()

# Initialize components for Routine "angerroutine"
angerroutineClock = core.Clock()
win.allowStencil = True
angerform = visual.Form(win=win, name='angerform',
    items='aboutanger.csv',
    textHeight=0.03,
    font='Open Sans',
    randomize=False,
    style='dark',
    fillColor=None, borderColor=None, itemColor='white', 
    responseColor='white', markerColor='red', colorSpace='rgb', 
    size=(1.5, 0.8),
    pos=(0, 0),
    itemPadding=0.05
)
angerContinuePrompt = visual.TextStim(win=win, name='angerContinuePrompt',
    text='Press Space to Submit and Continue',
    font='Open Sans',
    pos=(0, -0.45), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
angerKey = keyboard.Keyboard()

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
    size=(1.5, 0.8),
    pos=(0, 0),
    itemPadding=0.05
)
demoContinuePrompt = visual.TextStim(win=win, name='demoContinuePrompt',
    text='Press Space to Submit and Continue',
    font='Open Sans',
    pos=(0, -0.45), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
demoKey = keyboard.Keyboard()

# Initialize components for Routine "finish"
finishClock = core.Clock()
completetext = visual.TextStim(win=win, name='completetext',
    text='Study Complete',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
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
feedbackContinuePrompt = visual.TextStim(win=win, name='feedbackContinuePrompt',
    text='Press Space to Submit and Continue',
    font='Open Sans',
    pos=(0, -0.45), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
feedbackKey = keyboard.Keyboard()

# Initialize components for Routine "debrief"
debriefClock = core.Clock()
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
debriefContinuePrompt = visual.TextStim(win=win, name='debriefContinuePrompt',
    text='Press Space to Submit and Continue',
    font='Open Sans',
    pos=(0, -0.45), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
debriefKey = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
setupComponents = []
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
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "informationletter"-------
continueRoutine = True
# update component parameters for each repeat
infoKey.keys = []
infoKey.rt = []
_infoKey_allKeys = []
# keep track of which components have finished
informationletterComponents = [infoletter, infoContinuePrompt, infoKey]
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
    
    # *infoletter* updates
    if infoletter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        infoletter.frameNStart = frameN  # exact frame index
        infoletter.tStart = t  # local t and not account for scr refresh
        infoletter.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(infoletter, 'tStartRefresh')  # time at next scr refresh
        infoletter.setAutoDraw(True)
    
    # *infoContinuePrompt* updates
    if infoContinuePrompt.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        infoContinuePrompt.frameNStart = frameN  # exact frame index
        infoContinuePrompt.tStart = t  # local t and not account for scr refresh
        infoContinuePrompt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(infoContinuePrompt, 'tStartRefresh')  # time at next scr refresh
        infoContinuePrompt.setAutoDraw(True)
    
    # *infoKey* updates
    waitOnFlip = False
    if infoKey.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        infoKey.frameNStart = frameN  # exact frame index
        infoKey.tStart = t  # local t and not account for scr refresh
        infoKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(infoKey, 'tStartRefresh')  # time at next scr refresh
        infoKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(infoKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(infoKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if infoKey.status == STARTED and not waitOnFlip:
        theseKeys = infoKey.getKeys(keyList=['space'], waitRelease=False)
        _infoKey_allKeys.extend(theseKeys)
        if len(_infoKey_allKeys):
            infoKey.keys = _infoKey_allKeys[-1].name  # just the last key pressed
            infoKey.rt = _infoKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
consentKey.keys = []
consentKey.rt = []
_consentKey_allKeys = []
# keep track of which components have finished
consentComponents = [consentform, consentContinuePrompt, consentKey]
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
    
    # *consentform* updates
    if consentform.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        consentform.frameNStart = frameN  # exact frame index
        consentform.tStart = t  # local t and not account for scr refresh
        consentform.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consentform, 'tStartRefresh')  # time at next scr refresh
        consentform.setAutoDraw(True)
    
    # *consentContinuePrompt* updates
    if consentContinuePrompt.status == NOT_STARTED and consentform.formComplete():
        # keep track of start time/frame for later
        consentContinuePrompt.frameNStart = frameN  # exact frame index
        consentContinuePrompt.tStart = t  # local t and not account for scr refresh
        consentContinuePrompt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consentContinuePrompt, 'tStartRefresh')  # time at next scr refresh
        consentContinuePrompt.setAutoDraw(True)
    
    # *consentKey* updates
    waitOnFlip = False
    if consentKey.status == NOT_STARTED and consentform.formComplete():
        # keep track of start time/frame for later
        consentKey.frameNStart = frameN  # exact frame index
        consentKey.tStart = t  # local t and not account for scr refresh
        consentKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consentKey, 'tStartRefresh')  # time at next scr refresh
        consentKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(consentKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(consentKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if consentKey.status == STARTED and not waitOnFlip:
        theseKeys = consentKey.getKeys(keyList=['space'], waitRelease=False)
        _consentKey_allKeys.extend(theseKeys)
        if len(_consentKey_allKeys):
            consentKey.keys = _consentKey_allKeys[-1].name  # just the last key pressed
            consentKey.rt = _consentKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
consentform.addDataToExp(thisExp, 'rows')
consentform.autodraw = False
# the Routine "consent" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
instructKey.keys = []
instructKey.rt = []
_instructKey_allKeys = []
# keep track of which components have finished
instructionsComponents = [instructionsform, instructContinuePrompt, instructKey]
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
    
    # *instructionsform* updates
    if instructionsform.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionsform.frameNStart = frameN  # exact frame index
        instructionsform.tStart = t  # local t and not account for scr refresh
        instructionsform.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionsform, 'tStartRefresh')  # time at next scr refresh
        instructionsform.setAutoDraw(True)
    
    # *instructContinuePrompt* updates
    if instructContinuePrompt.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        instructContinuePrompt.frameNStart = frameN  # exact frame index
        instructContinuePrompt.tStart = t  # local t and not account for scr refresh
        instructContinuePrompt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructContinuePrompt, 'tStartRefresh')  # time at next scr refresh
        instructContinuePrompt.setAutoDraw(True)
    
    # *instructKey* updates
    waitOnFlip = False
    if instructKey.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        instructKey.frameNStart = frameN  # exact frame index
        instructKey.tStart = t  # local t and not account for scr refresh
        instructKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructKey, 'tStartRefresh')  # time at next scr refresh
        instructKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructKey.status == STARTED and not waitOnFlip:
        theseKeys = instructKey.getKeys(keyList=['space'], waitRelease=False)
        _instructKey_allKeys.extend(theseKeys)
        if len(_instructKey_allKeys):
            instructKey.keys = _instructKey_allKeys[-1].name  # just the last key pressed
            instructKey.rt = _instructKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
instructionsform.addDataToExp(thisExp, 'rows')
instructionsform.autodraw = False
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pranksLoop = data.TrialHandler(nReps=pranks.length, method='sequential', 
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
    promptLoop = data.TrialHandler(nReps=prompts.length, method='sequential', 
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
        
        sliderAnswered = false
        answerKey.keys = []
        answerKey.rt = []
        _answerKey_allKeys = []
        # keep track of which components have finished
        answerComponents = [prankText, promptText, hiddenobserver, slider, primertext, answerContinuePrompt, answerKey]
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
            
            # *primertext* updates
            if primertext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                primertext.frameNStart = frameN  # exact frame index
                primertext.tStart = t  # local t and not account for scr refresh
                primertext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(primertext, 'tStartRefresh')  # time at next scr refresh
                primertext.setAutoDraw(True)
            if primertext.status == STARTED:
                if frameN >= 20:
                    # keep track of stop time/frame for later
                    primertext.tStop = t  # not accounting for scr refresh
                    primertext.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(primertext, 'tStopRefresh')  # time at next scr refresh
                    primertext.setAutoDraw(False)
            
            # *answerContinuePrompt* updates
            if answerContinuePrompt.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                answerContinuePrompt.frameNStart = frameN  # exact frame index
                answerContinuePrompt.tStart = t  # local t and not account for scr refresh
                answerContinuePrompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(answerContinuePrompt, 'tStartRefresh')  # time at next scr refresh
                answerContinuePrompt.setAutoDraw(True)
            slider.getRating()
            if slider.getRating() is not None:
                sliderAnswered = true
            
            # *answerKey* updates
            waitOnFlip = False
            if answerKey.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                answerKey.frameNStart = frameN  # exact frame index
                answerKey.tStart = t  # local t and not account for scr refresh
                answerKey.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(answerKey, 'tStartRefresh')  # time at next scr refresh
                answerKey.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(answerKey.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(answerKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if answerKey.status == STARTED and not waitOnFlip:
                theseKeys = answerKey.getKeys(keyList=['space'], waitRelease=False)
                _answerKey_allKeys.extend(theseKeys)
                if len(_answerKey_allKeys):
                    answerKey.keys = _answerKey_allKeys[-1].name  # just the last key pressed
                    answerKey.rt = _answerKey_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
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
        sliderAnswered = false
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
        
    # completed prompts.length repeats of 'promptLoop'
    
    
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
    
# completed pranks.length repeats of 'pranksLoop'


# ------Prepare to start Routine "respectroutine"-------
continueRoutine = True
# update component parameters for each repeat
respectKey.keys = []
respectKey.rt = []
_respectKey_allKeys = []
# keep track of which components have finished
respectroutineComponents = [respectform, respectContinuePrompt, respectKey]
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
    
    # *respectContinuePrompt* updates
    if respectContinuePrompt.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        respectContinuePrompt.frameNStart = frameN  # exact frame index
        respectContinuePrompt.tStart = t  # local t and not account for scr refresh
        respectContinuePrompt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(respectContinuePrompt, 'tStartRefresh')  # time at next scr refresh
        respectContinuePrompt.setAutoDraw(True)
    
    # *respectKey* updates
    waitOnFlip = False
    if respectKey.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        respectKey.frameNStart = frameN  # exact frame index
        respectKey.tStart = t  # local t and not account for scr refresh
        respectKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(respectKey, 'tStartRefresh')  # time at next scr refresh
        respectKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(respectKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(respectKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if respectKey.status == STARTED and not waitOnFlip:
        theseKeys = respectKey.getKeys(keyList=['space'], waitRelease=False)
        _respectKey_allKeys.extend(theseKeys)
        if len(_respectKey_allKeys):
            respectKey.keys = _respectKey_allKeys[-1].name  # just the last key pressed
            respectKey.rt = _respectKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
angerKey.keys = []
angerKey.rt = []
_angerKey_allKeys = []
# keep track of which components have finished
angerroutineComponents = [angerform, angerContinuePrompt, angerKey]
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
    
    # *angerform* updates
    if angerform.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        angerform.frameNStart = frameN  # exact frame index
        angerform.tStart = t  # local t and not account for scr refresh
        angerform.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(angerform, 'tStartRefresh')  # time at next scr refresh
        angerform.setAutoDraw(True)
    
    # *angerContinuePrompt* updates
    if angerContinuePrompt.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        angerContinuePrompt.frameNStart = frameN  # exact frame index
        angerContinuePrompt.tStart = t  # local t and not account for scr refresh
        angerContinuePrompt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(angerContinuePrompt, 'tStartRefresh')  # time at next scr refresh
        angerContinuePrompt.setAutoDraw(True)
    
    # *angerKey* updates
    waitOnFlip = False
    if angerKey.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        angerKey.frameNStart = frameN  # exact frame index
        angerKey.tStart = t  # local t and not account for scr refresh
        angerKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(angerKey, 'tStartRefresh')  # time at next scr refresh
        angerKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(angerKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(angerKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if angerKey.status == STARTED and not waitOnFlip:
        theseKeys = angerKey.getKeys(keyList=['space'], waitRelease=False)
        _angerKey_allKeys.extend(theseKeys)
        if len(_angerKey_allKeys):
            angerKey.keys = _angerKey_allKeys[-1].name  # just the last key pressed
            angerKey.rt = _angerKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
demoKey.keys = []
demoKey.rt = []
_demoKey_allKeys = []
# keep track of which components have finished
demoroutineComponents = [demoForm, demoContinuePrompt, demoKey]
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
    
    # *demoContinuePrompt* updates
    if demoContinuePrompt.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        demoContinuePrompt.frameNStart = frameN  # exact frame index
        demoContinuePrompt.tStart = t  # local t and not account for scr refresh
        demoContinuePrompt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoContinuePrompt, 'tStartRefresh')  # time at next scr refresh
        demoContinuePrompt.setAutoDraw(True)
    
    # *demoKey* updates
    waitOnFlip = False
    if demoKey.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        demoKey.frameNStart = frameN  # exact frame index
        demoKey.tStart = t  # local t and not account for scr refresh
        demoKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoKey, 'tStartRefresh')  # time at next scr refresh
        demoKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(demoKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(demoKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if demoKey.status == STARTED and not waitOnFlip:
        theseKeys = demoKey.getKeys(keyList=['space'], waitRelease=False)
        _demoKey_allKeys.extend(theseKeys)
        if len(_demoKey_allKeys):
            demoKey.keys = _demoKey_allKeys[-1].name  # just the last key pressed
            demoKey.rt = _demoKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
finishComponents = [completetext]
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
    
    # *completetext* updates
    if completetext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        completetext.frameNStart = frameN  # exact frame index
        completetext.tStart = t  # local t and not account for scr refresh
        completetext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(completetext, 'tStartRefresh')  # time at next scr refresh
        completetext.setAutoDraw(True)
    if completetext.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > completetext.tStartRefresh + 1.00-frameTolerance:
            # keep track of stop time/frame for later
            completetext.tStop = t  # not accounting for scr refresh
            completetext.frameNStop = frameN  # exact frame index
            win.timeOnFlip(completetext, 'tStopRefresh')  # time at next scr refresh
            completetext.setAutoDraw(False)
    
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
feedbackKey.keys = []
feedbackKey.rt = []
_feedbackKey_allKeys = []
# keep track of which components have finished
feedbackComponents = [feedbackform, feedbackContinuePrompt, feedbackKey]
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
    
    # *feedbackform* updates
    if feedbackform.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        feedbackform.frameNStart = frameN  # exact frame index
        feedbackform.tStart = t  # local t and not account for scr refresh
        feedbackform.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedbackform, 'tStartRefresh')  # time at next scr refresh
        feedbackform.setAutoDraw(True)
    
    # *feedbackContinuePrompt* updates
    if feedbackContinuePrompt.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        feedbackContinuePrompt.frameNStart = frameN  # exact frame index
        feedbackContinuePrompt.tStart = t  # local t and not account for scr refresh
        feedbackContinuePrompt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedbackContinuePrompt, 'tStartRefresh')  # time at next scr refresh
        feedbackContinuePrompt.setAutoDraw(True)
    
    # *feedbackKey* updates
    waitOnFlip = False
    if feedbackKey.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        feedbackKey.frameNStart = frameN  # exact frame index
        feedbackKey.tStart = t  # local t and not account for scr refresh
        feedbackKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedbackKey, 'tStartRefresh')  # time at next scr refresh
        feedbackKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(feedbackKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(feedbackKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if feedbackKey.status == STARTED and not waitOnFlip:
        theseKeys = feedbackKey.getKeys(keyList=['space'], waitRelease=False)
        _feedbackKey_allKeys.extend(theseKeys)
        if len(_feedbackKey_allKeys):
            feedbackKey.keys = _feedbackKey_allKeys[-1].name  # just the last key pressed
            feedbackKey.rt = _feedbackKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
feedbackform.addDataToExp(thisExp, 'rows')
feedbackform.autodraw = False
# the Routine "feedback" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "debrief"-------
continueRoutine = True
# update component parameters for each repeat
debriefKey.keys = []
debriefKey.rt = []
_debriefKey_allKeys = []
# keep track of which components have finished
debriefComponents = [debriefform, debriefContinuePrompt, debriefKey]
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
    
    # *debriefform* updates
    if debriefform.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        debriefform.frameNStart = frameN  # exact frame index
        debriefform.tStart = t  # local t and not account for scr refresh
        debriefform.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(debriefform, 'tStartRefresh')  # time at next scr refresh
        debriefform.setAutoDraw(True)
    
    # *debriefContinuePrompt* updates
    if debriefContinuePrompt.status == NOT_STARTED and debriefform.formComplete():
        # keep track of start time/frame for later
        debriefContinuePrompt.frameNStart = frameN  # exact frame index
        debriefContinuePrompt.tStart = t  # local t and not account for scr refresh
        debriefContinuePrompt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(debriefContinuePrompt, 'tStartRefresh')  # time at next scr refresh
        debriefContinuePrompt.setAutoDraw(True)
    
    # *debriefKey* updates
    waitOnFlip = False
    if debriefKey.status == NOT_STARTED and debriefform.formComplete():
        # keep track of start time/frame for later
        debriefKey.frameNStart = frameN  # exact frame index
        debriefKey.tStart = t  # local t and not account for scr refresh
        debriefKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(debriefKey, 'tStartRefresh')  # time at next scr refresh
        debriefKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(debriefKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(debriefKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if debriefKey.status == STARTED and not waitOnFlip:
        theseKeys = debriefKey.getKeys(keyList=['space'], waitRelease=False)
        _debriefKey_allKeys.extend(theseKeys)
        if len(_debriefKey_allKeys):
            debriefKey.keys = _debriefKey_allKeys[-1].name  # just the last key pressed
            debriefKey.rt = _debriefKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
