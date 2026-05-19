------------
CL-Drive
------------

CL-Drive is a driver's cognitive load assessment dataset that contains physiological signals Electroencephalogram (EEG), Electrocardiography (ECG) and Electrodermal Activity (EDA) along with the eye-traking data. We have collected the EEG data using Muse S headband with 4 channels, ECG and EDA data are collected using the shimmers and Tobii is used to collect the Gaze data. The data is collected from 21 participants suring driving in an immersive simulated vehicle. The participants drove in 9 different complexity levels for 3 minutes each which helped induced different cognitive load among the participants. Please view our paper "Multimodal Brain-Computer Interface for In-Vehicle Driver Cognitive Load Measurement" for more details.

----------------
DATA STRUCTURE
----------------

CL-Drive
    |----EEG 
         |----participant_ID_1
                      |----eeg_data_level_1
                      |----eeg_baseline_level_1
                      .
                      .
                      .
                      |----eeg_data_level_9
                      |----eeg_baseline_level_9
         .
         .
         .
         |----participant_ID_21
    |----ECG
    |----EDA
    |----Gaze
    |----Labels


----------------------
DATA DESCRIPTION
----------------------

./                  : Root folder (contains all the raw data)
./EEG               : EEG data from all the participants
./ECG               : ECG data from all the participants
./EDA               : EDA data from all the participants
./Gaze              : Gaze data from all the participants
./Labels            : Labels data from all the participants

---------------------------------------------------------------------------------------------------------------------------

./EEG/1030          : EEG data and baseline for all 9 complexity levels from participants 1 
./EEG/1105          : EEG data and baseline for all 9 complexity levels from participants 2
.
.
.
./EEG/1953          : EEG data and baseline for all 9 complexity levels from participants 21

---------------------------------------------------------------------------------------------------------------------------

./ECG/1030          : ECG data and baseline for all 9 complexity levels from participants 1 
./ECG/1105          : ECG data and baseline for all 9 complexity levels from participants 2
.
.
.
./ECG/1953          : ECG data and baseline for all 9 complexity levels from participants 21

---------------------------------------------------------------------------------------------------------------------------

./EDA/1030          : EDA data and baseline for all 9 complexity levels from participants 1 
./EDA/1105          : EDA data and baseline for all 9 complexity levels from participants 2
.
.
.
./EDA/1953          : EDA data and baseline for all 9 complexity levels from participants 21

---------------------------------------------------------------------------------------------------------------------------

./Gaze/1030         : Gaze data and baseline for all 9 complexity levels from participants 1 
./Gaze/1105         : Gaze data and baseline for all 9 complexity levels from participants 2
.
.
.
./Gaze/1953         : Gaze data and baseline for all 9 complexity levels from participants 21

---------------------------------------------------------------------------------------------------------------------------

./Labels/1030       : Subjective cognitive load scores every 10 seconds for all 9 complexity levels from participant 1
./Labels/1105       : Subjective cognitive load scores every 10 seconds for all 9 complexity levels from participant 2
.
.
.
./Labels/1953       : Subjective cognitive load scores every 10 seconds for all 9 complexity levels from participant 21

-------------------------------------------------------------------------------








