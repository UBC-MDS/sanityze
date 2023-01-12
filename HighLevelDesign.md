# Sanityze High-level Design

## 1. Overview
Data used by data scientists to train and validate ML models,  should not contain personally identifiable information (PII). 

We occasionally have additional data about the people whose identities we want to conceal or redact. Occasionally we don't, since it's there's no convenient and reliable way to do so within the model training workflow. 

With the help of this package, it is simple to seamlessly remove personal information from Pandas DataFrames, maintaining the confidentiality of the individuals we are attempting to protect.

## 2. Concepts and Usage

There are 2 main classes in the package to help with the removal of PII from data:
1. `Cleanser` - the main class that handles the sanitization of the data
2. `Spotter` - the class that handles the identification of PII in the data. The package comes with a number of default spotters, such as:
   1. CreditCardSpotter
   2. EmailSpotter
   3. SINSpotter
   4. PhoneNumberSpotter

```python
import sanityze
import pandas as pd

cleanser = sanityze.Cleanser()
cleanser.add_spotter(sanityze.SINSpotter(),hash=True)
cleanser.add_spotter(sanityze.EmailSpotter())
df = pd.DataFrame(...)
cleansed_df = cleanser.clean(df)
```

### 3. APIs

### 3.1 Cleanser
Cleanser is a class that handles the sanitization of the data. Users can add/remove spotters to the cleanser, which will be used to identify PII in the data. The cleanser can then be used to cleanse the data. It has the following methods:
1. `add_spotter(spotter)` - adds a spotter to the cleanser
2. `add_all_spotters()` - adds all default spotters to the cleanser
3. `remove_spotter(spotter)` - removes a spotter from the cleanser
4. `clean(pd.DataFrame)` - takes a DataFrame and cleanses it, returning a new cleansed DataFrame

### 3.1 Spotters
Spotters are classes that handle the identification of PII in the data. The package comes with a number of default spotters, as subclasses. Users can also create their own spotters, as long as they implement the `Spotter` class.

