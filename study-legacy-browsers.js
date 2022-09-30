/************** 
 * Study Test *
 **************/


// store info about the experiment session:
let expName = 'study';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(setupRoutineBegin());
flowScheduler.add(setupRoutineEachFrame());
flowScheduler.add(setupRoutineEnd());
flowScheduler.add(informationletterRoutineBegin());
flowScheduler.add(informationletterRoutineEachFrame());
flowScheduler.add(informationletterRoutineEnd());
flowScheduler.add(consentRoutineBegin());
flowScheduler.add(consentRoutineEachFrame());
flowScheduler.add(consentRoutineEnd());
flowScheduler.add(instructionsRoutineBegin());
flowScheduler.add(instructionsRoutineEachFrame());
flowScheduler.add(instructionsRoutineEnd());
const pranksLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(pranksLoopLoopBegin(pranksLoopLoopScheduler));
flowScheduler.add(pranksLoopLoopScheduler);
flowScheduler.add(pranksLoopLoopEnd);
flowScheduler.add(respectroutineRoutineBegin());
flowScheduler.add(respectroutineRoutineEachFrame());
flowScheduler.add(respectroutineRoutineEnd());
flowScheduler.add(angerroutineRoutineBegin());
flowScheduler.add(angerroutineRoutineEachFrame());
flowScheduler.add(angerroutineRoutineEnd());
flowScheduler.add(demoroutineRoutineBegin());
flowScheduler.add(demoroutineRoutineEachFrame());
flowScheduler.add(demoroutineRoutineEnd());
flowScheduler.add(finishRoutineBegin());
flowScheduler.add(finishRoutineEachFrame());
flowScheduler.add(finishRoutineEnd());
flowScheduler.add(feedbackRoutineBegin());
flowScheduler.add(feedbackRoutineEachFrame());
flowScheduler.add(feedbackRoutineEnd());
flowScheduler.add(debriefRoutineBegin());
flowScheduler.add(debriefRoutineEachFrame());
flowScheduler.add(debriefRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'aboutanger.csv', 'path': 'aboutanger.csv'},
    {'name': 'consentform.csv', 'path': 'consentform.csv'},
    {'name': 'aboutrespect.csv', 'path': 'aboutrespect.csv'},
    {'name': 'feedbackletter.csv', 'path': 'feedbackletter.csv'},
    {'name': 'informationletter.csv', 'path': 'informationletter.csv'},
    {'name': 'demographic.csv', 'path': 'demographic.csv'},
    {'name': 'HO.csv', 'path': 'HO.csv'},
    {'name': 'debriefform.csv', 'path': 'debriefform.csv'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.1.4';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var setupClock;
var prompts;
var pranks;
var randomInt;
var primer;
var prankIndex;
var promptIndex;
var informationletterClock;
var infoletter;
var infoContinuePrompt;
var infoKey;
var consentClock;
var consentform;
var consentContinuePrompt;
var consentKey;
var instructionsClock;
var instructionsform;
var instructContinuePrompt;
var instructKey;
var numberClock;
var prankNumberText;
var answerClock;
var prankText;
var promptText;
var hiddenobserver;
var slider;
var primertext;
var answerContinuePrompt;
var answerKey;
var incrementPromptClock;
var incrementPrankClock;
var respectroutineClock;
var respectform;
var respectContinuePrompt;
var respectKey;
var angerroutineClock;
var angerform;
var angerContinuePrompt;
var angerKey;
var demoroutineClock;
var demoForm;
var demoContinuePrompt;
var demoKey;
var finishClock;
var completetext;
var feedbackClock;
var feedbackform;
var feedbackContinuePrompt;
var feedbackKey;
var debriefClock;
var debriefform;
var debriefContinuePrompt;
var debriefKey;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "setup"
  setupClock = new util.Clock();
  prompts = ["I think that what happened was funny.", "I definitely wouldn\u2019t have fallen for that prank.", "I feel bad for the target of the prank.", "I wish I could have been there to see that!", "The target just needs to move on \u2013 why do they need to tell the world about it?!", "I think that the prank went WAY too far."];
  pranks = ["\"Today my girlfriend decided it would be hilarious if she pulled a prank on me, so she did the classic \u2018bucket of water on a door\u2019 one. I ended up getting stitches and a concussion on my birthday.\" (3 July 2012)", "\"Today, my friends got me a cake for my birthday. As I blew out the candles, they shoved my head into it and I was knocked out for 3 minutes before an ambulance took me to the hospital. I got a concussion from a cake.\" (8 September 2017)", "\"Today, my friends decided to pull a prank. They told my girlfriend I had cheated on her, which I hadn\u2019t. Her revenge? Inviting me over to have me walk in on her with my brother. Our 6-month anniversary was two days away and I got her a trip to Spain, which cost me almost three paychecks.\" (19 December 2018)", "\"Today, while I was sleeping, my girlfriend took my phone and set the ringtone to a blood-curdling scream. I found this out when I received a call while driving to work and, thinking someone was being murdered in my backseat, I panicked and swerved into a parked car.\" (1 June 2011)", "\"Today, my sister called me at work and told me our elderly mom had passed away. I dropped everything and rushed home, to find out she was fine, and that my sister was just pranking me. When I explained this to my boss, he accused me of lying to get out of work, and I was fired.\" (6 July 2021)"];
  randomInt = util.randint(1, 4);
  primer = "error primer";
  prankIndex = 0;
  promptIndex = 0;
  
  // Initialize components for Routine "informationletter"
  informationletterClock = new util.Clock();
  infoletter = new visual.Form({
    win : psychoJS.window, name:'infoletter',
    items : 'informationletter.csv',
    textHeight : 0.03,
    font : 'Open Sans',
    randomize : false,
    size : [1.5, 0.8],
    pos : [0, 0],
    style : 'dark',
    itemPadding : 0.05
  });
  infoContinuePrompt = new visual.TextStim({
    win: psychoJS.window,
    name: 'infoContinuePrompt',
    text: 'Press Space to Submit and Continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.45)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  infoKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "consent"
  consentClock = new util.Clock();
  consentform = new visual.Form({
    win : psychoJS.window, name:'consentform',
    items : 'consentform.csv',
    textHeight : 0.03,
    font : 'Open Sans',
    randomize : false,
    size : [1.5, 0.8],
    pos : [0, 0],
    style : 'dark',
    itemPadding : 0.05
  });
  consentContinuePrompt = new visual.TextStim({
    win: psychoJS.window,
    name: 'consentContinuePrompt',
    text: 'Press Space to Submit and Continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.45)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  consentKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  instructionsform = new visual.Form({
    win : psychoJS.window, name:'instructionsform',
    items : 'HO.csv',
    textHeight : 0.03,
    font : 'Open Sans',
    randomize : false,
    size : [1.5, 0.8],
    pos : [0, 0],
    style : 'dark',
    itemPadding : 0.05
  });
  instructContinuePrompt = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructContinuePrompt',
    text: 'Press Space to Submit and Continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.45)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  instructKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "number"
  numberClock = new util.Clock();
  prankNumberText = new visual.TextStim({
    win: psychoJS.window,
    name: 'prankNumberText',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "answer"
  answerClock = new util.Clock();
  prankText = new visual.TextStim({
    win: psychoJS.window,
    name: 'prankText',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.2], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  promptText = new visual.TextStim({
    win: psychoJS.window,
    name: 'promptText',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.11)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  hiddenobserver = new visual.TextStim({
    win: psychoJS.window,
    name: 'hiddenobserver',
    text: 'My "hidden observer" says that:',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.05)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    size: [1.0, 0.07], pos: [0, (- 0.3)], units: 'height',
    labels: ["Strongly Disagree", "", "", "", "", "", "", "Strongly Agree"], fontSize: 0.05, ticks: [1, 2, 3, 4, 5, 6, 7, 8],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    fontFamily: 'Open Sans', bold: true, italic: false, depth: -3, 
    flip: true,
  });
  
  primertext = new visual.TextStim({
    win: psychoJS.window,
    name: 'primertext',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color([1.0, 1.0, 1.0]),  opacity: undefined,
    depth: 0.0 
  });
  
  answerContinuePrompt = new visual.TextStim({
    win: psychoJS.window,
    name: 'answerContinuePrompt',
    text: 'Press Space to Submit and Continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  answerKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "incrementPrompt"
  incrementPromptClock = new util.Clock();
  // Initialize components for Routine "incrementPrank"
  incrementPrankClock = new util.Clock();
  // Initialize components for Routine "respectroutine"
  respectroutineClock = new util.Clock();
  respectform = new visual.Form({
    win : psychoJS.window, name:'respectform',
    items : 'aboutrespect.csv',
    textHeight : 0.03,
    font : 'Open Sans',
    randomize : false,
    size : [1.5, 0.8],
    pos : [0, 0],
    style : 'dark',
    itemPadding : 0.05
  });
  respectContinuePrompt = new visual.TextStim({
    win: psychoJS.window,
    name: 'respectContinuePrompt',
    text: 'Press Space to Submit and Continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.45)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  respectKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "angerroutine"
  angerroutineClock = new util.Clock();
  angerform = new visual.Form({
    win : psychoJS.window, name:'angerform',
    items : 'aboutanger.csv',
    textHeight : 0.03,
    font : 'Open Sans',
    randomize : false,
    size : [1.5, 0.8],
    pos : [0, 0],
    style : 'dark',
    itemPadding : 0.05
  });
  angerContinuePrompt = new visual.TextStim({
    win: psychoJS.window,
    name: 'angerContinuePrompt',
    text: 'Press Space to Submit and Continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.45)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  angerKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "demoroutine"
  demoroutineClock = new util.Clock();
  demoForm = new visual.Form({
    win : psychoJS.window, name:'demoForm',
    items : 'demographic.csv',
    textHeight : 0.03,
    font : 'Open Sans',
    randomize : false,
    size : [1.5, 0.8],
    pos : [0, 0],
    style : 'dark',
    itemPadding : 0.05
  });
  demoContinuePrompt = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoContinuePrompt',
    text: 'Press Space to Submit and Continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.45)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  demoKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "finish"
  finishClock = new util.Clock();
  completetext = new visual.TextStim({
    win: psychoJS.window,
    name: 'completetext',
    text: 'Study Complete',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  feedbackform = new visual.Form({
    win : psychoJS.window, name:'feedbackform',
    items : 'feedbackletter.csv',
    textHeight : 0.03,
    font : 'Open Sans',
    randomize : false,
    size : [1, 0.8],
    pos : [0, 0],
    style : 'dark',
    itemPadding : 0.05
  });
  feedbackContinuePrompt = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedbackContinuePrompt',
    text: 'Press Space to Submit and Continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.45)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  feedbackKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "debrief"
  debriefClock = new util.Clock();
  debriefform = new visual.Form({
    win : psychoJS.window, name:'debriefform',
    items : 'debriefform.csv',
    textHeight : 0.03,
    font : 'Open Sans',
    randomize : false,
    size : [1, 0.8],
    pos : [0, 0],
    style : 'dark',
    itemPadding : 0.05
  });
  debriefContinuePrompt = new visual.TextStim({
    win: psychoJS.window,
    name: 'debriefContinuePrompt',
    text: 'Press Space to Submit and Continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.45)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  debriefKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var setupComponents;
function setupRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'setup'-------
    t = 0;
    setupClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    setupComponents = [];
    
    setupComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function setupRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'setup'-------
    // get current time
    t = setupClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    setupComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function setupRoutineEnd() {
  return async function () {
    //------Ending Routine 'setup'-------
    setupComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    if ((randomInt === 1)) {
        primer = "You're nothing";
    } else {
        if ((randomInt === 2)) {
            primer = "You're great";
        } else {
            if ((randomInt === 3)) {
                primer = "People are walking";
            } else {
                primer = "Error 2";
            }
        }
    }
    psychoJS.experiment.addData("study.primer", primer);
    
    // the Routine "setup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _infoKey_allKeys;
var informationletterComponents;
function informationletterRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'informationletter'-------
    t = 0;
    informationletterClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    infoKey.keys = undefined;
    infoKey.rt = undefined;
    _infoKey_allKeys = [];
    // keep track of which components have finished
    informationletterComponents = [];
    informationletterComponents.push(infoletter);
    informationletterComponents.push(infoContinuePrompt);
    informationletterComponents.push(infoKey);
    
    informationletterComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function informationletterRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'informationletter'-------
    // get current time
    t = informationletterClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *infoletter* updates
    if (t >= 0.0 && infoletter.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      infoletter.tStart = t;  // (not accounting for frame time here)
      infoletter.frameNStart = frameN;  // exact frame index
      
      infoletter.setAutoDraw(true);
    }

    
    // *infoContinuePrompt* updates
    if (t >= 0.5 && infoContinuePrompt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      infoContinuePrompt.tStart = t;  // (not accounting for frame time here)
      infoContinuePrompt.frameNStart = frameN;  // exact frame index
      
      infoContinuePrompt.setAutoDraw(true);
    }

    
    // *infoKey* updates
    if (t >= 0.5 && infoKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      infoKey.tStart = t;  // (not accounting for frame time here)
      infoKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { infoKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { infoKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { infoKey.clearEvents(); });
    }

    if (infoKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = infoKey.getKeys({keyList: ['space'], waitRelease: false});
      _infoKey_allKeys = _infoKey_allKeys.concat(theseKeys);
      if (_infoKey_allKeys.length > 0) {
        infoKey.keys = _infoKey_allKeys[_infoKey_allKeys.length - 1].name;  // just the last key pressed
        infoKey.rt = _infoKey_allKeys[_infoKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    informationletterComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function informationletterRoutineEnd() {
  return async function () {
    //------Ending Routine 'informationletter'-------
    informationletterComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    infoletter.addDataToExp(psychoJS.experiment, 'rows');
    infoKey.stop();
    // the Routine "informationletter" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _consentKey_allKeys;
var consentComponents;
function consentRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'consent'-------
    t = 0;
    consentClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    consentKey.keys = undefined;
    consentKey.rt = undefined;
    _consentKey_allKeys = [];
    // keep track of which components have finished
    consentComponents = [];
    consentComponents.push(consentform);
    consentComponents.push(consentContinuePrompt);
    consentComponents.push(consentKey);
    
    consentComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function consentRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'consent'-------
    // get current time
    t = consentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *consentform* updates
    if (t >= 0.0 && consentform.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consentform.tStart = t;  // (not accounting for frame time here)
      consentform.frameNStart = frameN;  // exact frame index
      
      consentform.setAutoDraw(true);
    }

    
    // *consentContinuePrompt* updates
    if ((consentform.formComplete()) && consentContinuePrompt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consentContinuePrompt.tStart = t;  // (not accounting for frame time here)
      consentContinuePrompt.frameNStart = frameN;  // exact frame index
      
      consentContinuePrompt.setAutoDraw(true);
    }

    
    // *consentKey* updates
    if ((consentform.formComplete()) && consentKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consentKey.tStart = t;  // (not accounting for frame time here)
      consentKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { consentKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { consentKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { consentKey.clearEvents(); });
    }

    if (consentKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = consentKey.getKeys({keyList: ['space'], waitRelease: false});
      _consentKey_allKeys = _consentKey_allKeys.concat(theseKeys);
      if (_consentKey_allKeys.length > 0) {
        consentKey.keys = _consentKey_allKeys[_consentKey_allKeys.length - 1].name;  // just the last key pressed
        consentKey.rt = _consentKey_allKeys[_consentKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    consentComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function consentRoutineEnd() {
  return async function () {
    //------Ending Routine 'consent'-------
    consentComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    consentform.addDataToExp(psychoJS.experiment, 'rows');
    consentKey.stop();
    // the Routine "consent" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _instructKey_allKeys;
var instructionsComponents;
function instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'instructions'-------
    t = 0;
    instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    instructKey.keys = undefined;
    instructKey.rt = undefined;
    _instructKey_allKeys = [];
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(instructionsform);
    instructionsComponents.push(instructContinuePrompt);
    instructionsComponents.push(instructKey);
    
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructionsRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'instructions'-------
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructionsform* updates
    if (t >= 0.0 && instructionsform.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructionsform.tStart = t;  // (not accounting for frame time here)
      instructionsform.frameNStart = frameN;  // exact frame index
      
      instructionsform.setAutoDraw(true);
    }

    
    // *instructContinuePrompt* updates
    if (t >= 0.5 && instructContinuePrompt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructContinuePrompt.tStart = t;  // (not accounting for frame time here)
      instructContinuePrompt.frameNStart = frameN;  // exact frame index
      
      instructContinuePrompt.setAutoDraw(true);
    }

    
    // *instructKey* updates
    if (t >= 0.5 && instructKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructKey.tStart = t;  // (not accounting for frame time here)
      instructKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instructKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instructKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instructKey.clearEvents(); });
    }

    if (instructKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = instructKey.getKeys({keyList: ['space'], waitRelease: false});
      _instructKey_allKeys = _instructKey_allKeys.concat(theseKeys);
      if (_instructKey_allKeys.length > 0) {
        instructKey.keys = _instructKey_allKeys[_instructKey_allKeys.length - 1].name;  // just the last key pressed
        instructKey.rt = _instructKey_allKeys[_instructKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionsRoutineEnd() {
  return async function () {
    //------Ending Routine 'instructions'-------
    instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    instructionsform.addDataToExp(psychoJS.experiment, 'rows');
    instructKey.stop();
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var pranksLoop;
var currentLoop;
function pranksLoopLoopBegin(pranksLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    pranksLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: pranks.length, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'pranksLoop'
    });
    psychoJS.experiment.addLoop(pranksLoop); // add the loop to the experiment
    currentLoop = pranksLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    pranksLoop.forEach(function() {
      const snapshot = pranksLoop.getSnapshot();
    
      pranksLoopLoopScheduler.add(importConditions(snapshot));
      pranksLoopLoopScheduler.add(numberRoutineBegin(snapshot));
      pranksLoopLoopScheduler.add(numberRoutineEachFrame());
      pranksLoopLoopScheduler.add(numberRoutineEnd());
      const promptLoopLoopScheduler = new Scheduler(psychoJS);
      pranksLoopLoopScheduler.add(promptLoopLoopBegin(promptLoopLoopScheduler, snapshot));
      pranksLoopLoopScheduler.add(promptLoopLoopScheduler);
      pranksLoopLoopScheduler.add(promptLoopLoopEnd);
      pranksLoopLoopScheduler.add(incrementPrankRoutineBegin(snapshot));
      pranksLoopLoopScheduler.add(incrementPrankRoutineEachFrame());
      pranksLoopLoopScheduler.add(incrementPrankRoutineEnd());
      pranksLoopLoopScheduler.add(endLoopIteration(pranksLoopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var promptLoop;
function promptLoopLoopBegin(promptLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    promptLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: prompts.length, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'promptLoop'
    });
    psychoJS.experiment.addLoop(promptLoop); // add the loop to the experiment
    currentLoop = promptLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    promptLoop.forEach(function() {
      const snapshot = promptLoop.getSnapshot();
    
      promptLoopLoopScheduler.add(importConditions(snapshot));
      promptLoopLoopScheduler.add(answerRoutineBegin(snapshot));
      promptLoopLoopScheduler.add(answerRoutineEachFrame());
      promptLoopLoopScheduler.add(answerRoutineEnd());
      promptLoopLoopScheduler.add(incrementPromptRoutineBegin(snapshot));
      promptLoopLoopScheduler.add(incrementPromptRoutineEachFrame());
      promptLoopLoopScheduler.add(incrementPromptRoutineEnd());
      promptLoopLoopScheduler.add(endLoopIteration(promptLoopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function promptLoopLoopEnd() {
  psychoJS.experiment.removeLoop(promptLoop);

  return Scheduler.Event.NEXT;
}


async function pranksLoopLoopEnd() {
  psychoJS.experiment.removeLoop(pranksLoop);

  return Scheduler.Event.NEXT;
}


var numberComponents;
function numberRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'number'-------
    t = 0;
    numberClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    prankNumberText.setText(("Prank " + (prankIndex + 1).toString()));
    // keep track of which components have finished
    numberComponents = [];
    numberComponents.push(prankNumberText);
    
    numberComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function numberRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'number'-------
    // get current time
    t = numberClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *prankNumberText* updates
    if (t >= 0.0 && prankNumberText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prankNumberText.tStart = t;  // (not accounting for frame time here)
      prankNumberText.frameNStart = frameN;  // exact frame index
      
      prankNumberText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prankNumberText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prankNumberText.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    numberComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function numberRoutineEnd() {
  return async function () {
    //------Ending Routine 'number'-------
    numberComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var prankVar;
var promptVar;
var sliderAnswered;
var _answerKey_allKeys;
var answerComponents;
function answerRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'answer'-------
    t = 0;
    answerClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    slider.reset()
    primertext.setText(primer);
    prankVar = pranks[prankIndex];
    promptVar = prompts[promptIndex];
    psychoJS.experiment.addData("prankVar.routineValue", ("\"" + prankVar));
    psychoJS.experiment.addData("promptVar.routineValue", (("\"" + promptVar) + "\""));
    sliderAnswered = false;
    
    answerKey.keys = undefined;
    answerKey.rt = undefined;
    _answerKey_allKeys = [];
    // keep track of which components have finished
    answerComponents = [];
    answerComponents.push(prankText);
    answerComponents.push(promptText);
    answerComponents.push(hiddenobserver);
    answerComponents.push(slider);
    answerComponents.push(primertext);
    answerComponents.push(answerContinuePrompt);
    answerComponents.push(answerKey);
    
    answerComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function answerRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'answer'-------
    // get current time
    t = answerClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *prankText* updates
    if (frameN >= 2 && prankText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prankText.tStart = t;  // (not accounting for frame time here)
      prankText.frameNStart = frameN;  // exact frame index
      
      prankText.setAutoDraw(true);
    }

    
    if (prankText.status === PsychoJS.Status.STARTED){ // only update if being drawn
      prankText.setText(prankVar, false);
    }
    
    // *promptText* updates
    if (frameN >= 2 && promptText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      promptText.tStart = t;  // (not accounting for frame time here)
      promptText.frameNStart = frameN;  // exact frame index
      
      promptText.setAutoDraw(true);
    }

    
    if (promptText.status === PsychoJS.Status.STARTED){ // only update if being drawn
      promptText.setText(promptVar, false);
    }
    
    // *hiddenobserver* updates
    if (frameN >= 2 && hiddenobserver.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      hiddenobserver.tStart = t;  // (not accounting for frame time here)
      hiddenobserver.frameNStart = frameN;  // exact frame index
      
      hiddenobserver.setAutoDraw(true);
    }

    
    // *slider* updates
    if (t >= 0.0 && slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider.tStart = t;  // (not accounting for frame time here)
      slider.frameNStart = frameN;  // exact frame index
      
      slider.setAutoDraw(true);
    }

    
    // *primertext* updates
    if (t >= 0.0 && primertext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      primertext.tStart = t;  // (not accounting for frame time here)
      primertext.frameNStart = frameN;  // exact frame index
      
      primertext.setAutoDraw(true);
    }

    if (primertext.status === PsychoJS.Status.STARTED && frameN >= 20) {
      primertext.setAutoDraw(false);
    }
    
    // *answerContinuePrompt* updates
    if (t >= 0.5 && answerContinuePrompt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answerContinuePrompt.tStart = t;  // (not accounting for frame time here)
      answerContinuePrompt.frameNStart = frameN;  // exact frame index
      
      answerContinuePrompt.setAutoDraw(true);
    }

    slider.getRating();
    if ((slider.getRating() !== null)) {
        sliderAnswered = true;
    }
    
    
    // *answerKey* updates
    if (t >= 0.5 && answerKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answerKey.tStart = t;  // (not accounting for frame time here)
      answerKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { answerKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { answerKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { answerKey.clearEvents(); });
    }

    if (answerKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = answerKey.getKeys({keyList: ['space'], waitRelease: false});
      _answerKey_allKeys = _answerKey_allKeys.concat(theseKeys);
      if (_answerKey_allKeys.length > 0) {
        answerKey.keys = _answerKey_allKeys[_answerKey_allKeys.length - 1].name;  // just the last key pressed
        answerKey.rt = _answerKey_allKeys[_answerKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    answerComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function answerRoutineEnd() {
  return async function () {
    //------Ending Routine 'answer'-------
    answerComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('slider.response', slider.getRating());
    psychoJS.experiment.addData('slider.rt', slider.getRT());
    sliderAnswered = false;
    
    answerKey.stop();
    // the Routine "answer" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var incrementPromptComponents;
function incrementPromptRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'incrementPrompt'-------
    t = 0;
    incrementPromptClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    promptIndex = (promptIndex + 1);
    
    // keep track of which components have finished
    incrementPromptComponents = [];
    
    incrementPromptComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function incrementPromptRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'incrementPrompt'-------
    // get current time
    t = incrementPromptClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    incrementPromptComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function incrementPromptRoutineEnd() {
  return async function () {
    //------Ending Routine 'incrementPrompt'-------
    incrementPromptComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "incrementPrompt" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var incrementPrankComponents;
function incrementPrankRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'incrementPrank'-------
    t = 0;
    incrementPrankClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    prankIndex = (prankIndex + 1);
    promptIndex = 0;
    
    // keep track of which components have finished
    incrementPrankComponents = [];
    
    incrementPrankComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function incrementPrankRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'incrementPrank'-------
    // get current time
    t = incrementPrankClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    incrementPrankComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function incrementPrankRoutineEnd() {
  return async function () {
    //------Ending Routine 'incrementPrank'-------
    incrementPrankComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "incrementPrank" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _respectKey_allKeys;
var respectroutineComponents;
function respectroutineRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'respectroutine'-------
    t = 0;
    respectroutineClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    respectKey.keys = undefined;
    respectKey.rt = undefined;
    _respectKey_allKeys = [];
    // keep track of which components have finished
    respectroutineComponents = [];
    respectroutineComponents.push(respectform);
    respectroutineComponents.push(respectContinuePrompt);
    respectroutineComponents.push(respectKey);
    
    respectroutineComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function respectroutineRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'respectroutine'-------
    // get current time
    t = respectroutineClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *respectform* updates
    if (t >= 0.0 && respectform.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      respectform.tStart = t;  // (not accounting for frame time here)
      respectform.frameNStart = frameN;  // exact frame index
      
      respectform.setAutoDraw(true);
    }

    
    // *respectContinuePrompt* updates
    if (t >= 0.5 && respectContinuePrompt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      respectContinuePrompt.tStart = t;  // (not accounting for frame time here)
      respectContinuePrompt.frameNStart = frameN;  // exact frame index
      
      respectContinuePrompt.setAutoDraw(true);
    }

    
    // *respectKey* updates
    if (t >= 0.5 && respectKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      respectKey.tStart = t;  // (not accounting for frame time here)
      respectKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { respectKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { respectKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { respectKey.clearEvents(); });
    }

    if (respectKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = respectKey.getKeys({keyList: ['space'], waitRelease: false});
      _respectKey_allKeys = _respectKey_allKeys.concat(theseKeys);
      if (_respectKey_allKeys.length > 0) {
        respectKey.keys = _respectKey_allKeys[_respectKey_allKeys.length - 1].name;  // just the last key pressed
        respectKey.rt = _respectKey_allKeys[_respectKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    respectroutineComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function respectroutineRoutineEnd() {
  return async function () {
    //------Ending Routine 'respectroutine'-------
    respectroutineComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    respectform.addDataToExp(psychoJS.experiment, 'rows');
    respectKey.stop();
    // the Routine "respectroutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _angerKey_allKeys;
var angerroutineComponents;
function angerroutineRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'angerroutine'-------
    t = 0;
    angerroutineClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    angerKey.keys = undefined;
    angerKey.rt = undefined;
    _angerKey_allKeys = [];
    // keep track of which components have finished
    angerroutineComponents = [];
    angerroutineComponents.push(angerform);
    angerroutineComponents.push(angerContinuePrompt);
    angerroutineComponents.push(angerKey);
    
    angerroutineComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function angerroutineRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'angerroutine'-------
    // get current time
    t = angerroutineClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *angerform* updates
    if (t >= 0.0 && angerform.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      angerform.tStart = t;  // (not accounting for frame time here)
      angerform.frameNStart = frameN;  // exact frame index
      
      angerform.setAutoDraw(true);
    }

    
    // *angerContinuePrompt* updates
    if (t >= 0.5 && angerContinuePrompt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      angerContinuePrompt.tStart = t;  // (not accounting for frame time here)
      angerContinuePrompt.frameNStart = frameN;  // exact frame index
      
      angerContinuePrompt.setAutoDraw(true);
    }

    
    // *angerKey* updates
    if (t >= 0.5 && angerKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      angerKey.tStart = t;  // (not accounting for frame time here)
      angerKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { angerKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { angerKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { angerKey.clearEvents(); });
    }

    if (angerKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = angerKey.getKeys({keyList: ['space'], waitRelease: false});
      _angerKey_allKeys = _angerKey_allKeys.concat(theseKeys);
      if (_angerKey_allKeys.length > 0) {
        angerKey.keys = _angerKey_allKeys[_angerKey_allKeys.length - 1].name;  // just the last key pressed
        angerKey.rt = _angerKey_allKeys[_angerKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    angerroutineComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function angerroutineRoutineEnd() {
  return async function () {
    //------Ending Routine 'angerroutine'-------
    angerroutineComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    angerform.addDataToExp(psychoJS.experiment, 'rows');
    angerKey.stop();
    // the Routine "angerroutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _demoKey_allKeys;
var demoroutineComponents;
function demoroutineRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'demoroutine'-------
    t = 0;
    demoroutineClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    demoKey.keys = undefined;
    demoKey.rt = undefined;
    _demoKey_allKeys = [];
    // keep track of which components have finished
    demoroutineComponents = [];
    demoroutineComponents.push(demoForm);
    demoroutineComponents.push(demoContinuePrompt);
    demoroutineComponents.push(demoKey);
    
    demoroutineComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function demoroutineRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'demoroutine'-------
    // get current time
    t = demoroutineClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *demoForm* updates
    if (t >= 0.0 && demoForm.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoForm.tStart = t;  // (not accounting for frame time here)
      demoForm.frameNStart = frameN;  // exact frame index
      
      demoForm.setAutoDraw(true);
    }

    
    // *demoContinuePrompt* updates
    if (t >= 0.5 && demoContinuePrompt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoContinuePrompt.tStart = t;  // (not accounting for frame time here)
      demoContinuePrompt.frameNStart = frameN;  // exact frame index
      
      demoContinuePrompt.setAutoDraw(true);
    }

    
    // *demoKey* updates
    if (t >= 0.5 && demoKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoKey.tStart = t;  // (not accounting for frame time here)
      demoKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { demoKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { demoKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { demoKey.clearEvents(); });
    }

    if (demoKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = demoKey.getKeys({keyList: ['space'], waitRelease: false});
      _demoKey_allKeys = _demoKey_allKeys.concat(theseKeys);
      if (_demoKey_allKeys.length > 0) {
        demoKey.keys = _demoKey_allKeys[_demoKey_allKeys.length - 1].name;  // just the last key pressed
        demoKey.rt = _demoKey_allKeys[_demoKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    demoroutineComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function demoroutineRoutineEnd() {
  return async function () {
    //------Ending Routine 'demoroutine'-------
    demoroutineComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    demoForm.addDataToExp(psychoJS.experiment, 'rows');
    demoKey.stop();
    // the Routine "demoroutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var finishComponents;
function finishRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'finish'-------
    t = 0;
    finishClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    finishComponents = [];
    finishComponents.push(completetext);
    
    finishComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function finishRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'finish'-------
    // get current time
    t = finishClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *completetext* updates
    if (t >= 0.0 && completetext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      completetext.tStart = t;  // (not accounting for frame time here)
      completetext.frameNStart = frameN;  // exact frame index
      
      completetext.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (completetext.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      completetext.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    finishComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function finishRoutineEnd() {
  return async function () {
    //------Ending Routine 'finish'-------
    finishComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _feedbackKey_allKeys;
var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'feedback'-------
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    feedbackKey.keys = undefined;
    feedbackKey.rt = undefined;
    _feedbackKey_allKeys = [];
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(feedbackform);
    feedbackComponents.push(feedbackContinuePrompt);
    feedbackComponents.push(feedbackKey);
    
    feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function feedbackRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'feedback'-------
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedbackform* updates
    if (t >= 0.0 && feedbackform.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedbackform.tStart = t;  // (not accounting for frame time here)
      feedbackform.frameNStart = frameN;  // exact frame index
      
      feedbackform.setAutoDraw(true);
    }

    
    // *feedbackContinuePrompt* updates
    if (t >= 0.5 && feedbackContinuePrompt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedbackContinuePrompt.tStart = t;  // (not accounting for frame time here)
      feedbackContinuePrompt.frameNStart = frameN;  // exact frame index
      
      feedbackContinuePrompt.setAutoDraw(true);
    }

    
    // *feedbackKey* updates
    if (t >= 0.5 && feedbackKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedbackKey.tStart = t;  // (not accounting for frame time here)
      feedbackKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { feedbackKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { feedbackKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { feedbackKey.clearEvents(); });
    }

    if (feedbackKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = feedbackKey.getKeys({keyList: ['space'], waitRelease: false});
      _feedbackKey_allKeys = _feedbackKey_allKeys.concat(theseKeys);
      if (_feedbackKey_allKeys.length > 0) {
        feedbackKey.keys = _feedbackKey_allKeys[_feedbackKey_allKeys.length - 1].name;  // just the last key pressed
        feedbackKey.rt = _feedbackKey_allKeys[_feedbackKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedbackRoutineEnd() {
  return async function () {
    //------Ending Routine 'feedback'-------
    feedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    feedbackform.addDataToExp(psychoJS.experiment, 'rows');
    feedbackKey.stop();
    // the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _debriefKey_allKeys;
var debriefComponents;
function debriefRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'debrief'-------
    t = 0;
    debriefClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    debriefKey.keys = undefined;
    debriefKey.rt = undefined;
    _debriefKey_allKeys = [];
    // keep track of which components have finished
    debriefComponents = [];
    debriefComponents.push(debriefform);
    debriefComponents.push(debriefContinuePrompt);
    debriefComponents.push(debriefKey);
    
    debriefComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function debriefRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'debrief'-------
    // get current time
    t = debriefClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *debriefform* updates
    if (t >= 0.0 && debriefform.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debriefform.tStart = t;  // (not accounting for frame time here)
      debriefform.frameNStart = frameN;  // exact frame index
      
      debriefform.setAutoDraw(true);
    }

    
    // *debriefContinuePrompt* updates
    if ((debriefform.formComplete()) && debriefContinuePrompt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debriefContinuePrompt.tStart = t;  // (not accounting for frame time here)
      debriefContinuePrompt.frameNStart = frameN;  // exact frame index
      
      debriefContinuePrompt.setAutoDraw(true);
    }

    
    // *debriefKey* updates
    if ((debriefform.formComplete()) && debriefKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debriefKey.tStart = t;  // (not accounting for frame time here)
      debriefKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { debriefKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { debriefKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { debriefKey.clearEvents(); });
    }

    if (debriefKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = debriefKey.getKeys({keyList: ['space'], waitRelease: false});
      _debriefKey_allKeys = _debriefKey_allKeys.concat(theseKeys);
      if (_debriefKey_allKeys.length > 0) {
        debriefKey.keys = _debriefKey_allKeys[_debriefKey_allKeys.length - 1].name;  // just the last key pressed
        debriefKey.rt = _debriefKey_allKeys[_debriefKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    debriefComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function debriefRoutineEnd() {
  return async function () {
    //------Ending Routine 'debrief'-------
    debriefComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    debriefform.addDataToExp(psychoJS.experiment, 'rows');
    debriefKey.stop();
    // the Routine "debrief" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
