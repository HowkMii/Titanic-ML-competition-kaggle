{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "_cell_guid": "16c439e1-c0d3-4258-ba8b-ddf6adb84c75",
    "_uuid": "f9786e60-8870-44c3-9c41-cfbb0df1c970"
   },
   "source": [
    "# Students performance in exams"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "_cell_guid": "592b00fd-0f0e-4238-87f0-236a6d50443e",
    "_uuid": "6495f96c-9371-45e7-b6b3-fc361b13c5f7",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-01-05T22:25:00.678441Z",
     "iopub.status.busy": "2022-01-05T22:25:00.677671Z",
     "iopub.status.idle": "2022-01-05T22:25:00.775896Z",
     "shell.execute_reply": "2022-01-05T22:25:00.774993Z",
     "shell.execute_reply.started": "2022-01-05T22:25:00.678364Z"
    },
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline\n",
    "\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.svm import SVC, LinearSVC\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "from sklearn.naive_bayes import GaussianNB\n",
    "from sklearn.linear_model import Perceptron\n",
    "from sklearn.linear_model import SGDClassifier\n",
    "from sklearn.tree import DecisionTreeClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "_cell_guid": "ee046f87-f242-436c-8833-b705f4692344",
    "_uuid": "56e90bec-54f3-48f5-a528-89ff5b5441f0",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-01-05T20:08:36.168579Z",
     "iopub.status.busy": "2022-01-05T20:08:36.168204Z",
     "iopub.status.idle": "2022-01-05T20:08:36.189418Z",
     "shell.execute_reply": "2022-01-05T20:08:36.188665Z",
     "shell.execute_reply.started": "2022-01-05T20:08:36.168518Z"
    },
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [],
   "source": [
    "data = pd.read_csv(\"../input/StudentsPerformance.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "_cell_guid": "a55ee3c5-8698-477f-979b-65bfa2ce9c43",
    "_uuid": "51dfa775-76be-4c9f-82e2-e3a1b4561a3a",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-01-05T20:08:36.191604Z",
     "iopub.status.busy": "2022-01-05T20:08:36.191054Z",
     "iopub.status.idle": "2022-01-05T20:08:36.222844Z",
     "shell.execute_reply": "2022-01-05T20:08:36.221602Z",
     "shell.execute_reply.started": "2022-01-05T20:08:36.191546Z"
    },
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>race/ethnicity</th>\n",
       "      <th>parental level of education</th>\n",
       "      <th>lunch</th>\n",
       "      <th>test preparation course</th>\n",
       "      <th>math score</th>\n",
       "      <th>reading score</th>\n",
       "      <th>writing score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>female</td>\n",
       "      <td>group B</td>\n",
       "      <td>bachelor's degree</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>72</td>\n",
       "      <td>72</td>\n",
       "      <td>74</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>female</td>\n",
       "      <td>group C</td>\n",
       "      <td>some college</td>\n",
       "      <td>standard</td>\n",
       "      <td>completed</td>\n",
       "      <td>69</td>\n",
       "      <td>90</td>\n",
       "      <td>88</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>female</td>\n",
       "      <td>group B</td>\n",
       "      <td>master's degree</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>90</td>\n",
       "      <td>95</td>\n",
       "      <td>93</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>male</td>\n",
       "      <td>group A</td>\n",
       "      <td>associate's degree</td>\n",
       "      <td>free/reduced</td>\n",
       "      <td>none</td>\n",
       "      <td>47</td>\n",
       "      <td>57</td>\n",
       "      <td>44</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>male</td>\n",
       "      <td>group C</td>\n",
       "      <td>some college</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>76</td>\n",
       "      <td>78</td>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   gender race/ethnicity      ...      reading score writing score\n",
       "0  female        group B      ...                 72            74\n",
       "1  female        group C      ...                 90            88\n",
       "2  female        group B      ...                 95            93\n",
       "3    male        group A      ...                 57            44\n",
       "4    male        group C      ...                 78            75\n",
       "\n",
       "[5 rows x 8 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "_cell_guid": "c5c6c630-3e84-49e5-abf9-c4ee694f0c96",
    "_uuid": "0f649605-b580-47d1-b3a6-24af30774d38",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-01-05T20:08:36.224668Z",
     "iopub.status.busy": "2022-01-05T20:08:36.224433Z",
     "iopub.status.idle": "2022-01-05T20:08:36.229759Z",
     "shell.execute_reply": "2022-01-05T20:08:36.228391Z",
     "shell.execute_reply.started": "2022-01-05T20:08:36.224633Z"
    },
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1000, 8)\n"
     ]
    }
   ],
   "source": [
    "print (data.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "_cell_guid": "f9fb7011-b157-435c-b17b-87ea2656b27a",
    "_uuid": "fe1771e6-5e8f-4068-ba97-4529a7356168",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-01-05T20:08:36.232040Z",
     "iopub.status.busy": "2022-01-05T20:08:36.231432Z",
     "iopub.status.idle": "2022-01-05T20:08:36.249744Z",
     "shell.execute_reply": "2022-01-05T20:08:36.248471Z",
     "shell.execute_reply.started": "2022-01-05T20:08:36.231767Z"
    },
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1000 entries, 0 to 999\n",
      "Data columns (total 8 columns):\n",
      "gender                         1000 non-null object\n",
      "race/ethnicity                 1000 non-null object\n",
      "parental level of education    1000 non-null object\n",
      "lunch                          1000 non-null object\n",
      "test preparation course        1000 non-null object\n",
      "math score                     1000 non-null int64\n",
      "reading score                  1000 non-null int64\n",
      "writing score                  1000 non-null int64\n",
      "dtypes: int64(3), object(5)\n",
      "memory usage: 62.6+ KB\n"
     ]
    }
   ],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "_cell_guid": "e238aece-91b5-478f-b03c-ad4341f5bb1c",
    "_uuid": "c26f81f9-53a1-43b6-9b70-27dbf43b61c0",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-01-05T20:08:36.251900Z",
     "iopub.status.busy": "2022-01-05T20:08:36.251557Z",
     "iopub.status.idle": "2022-01-05T20:08:36.282078Z",
     "shell.execute_reply": "2022-01-05T20:08:36.281087Z",
     "shell.execute_reply.started": "2022-01-05T20:08:36.251837Z"
    },
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>math score</th>\n",
       "      <th>reading score</th>\n",
       "      <th>writing score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>1000.00000</td>\n",
       "      <td>1000.000000</td>\n",
       "      <td>1000.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>66.08900</td>\n",
       "      <td>69.169000</td>\n",
       "      <td>68.054000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>15.16308</td>\n",
       "      <td>14.600192</td>\n",
       "      <td>15.195657</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.00000</td>\n",
       "      <td>17.000000</td>\n",
       "      <td>10.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>57.00000</td>\n",
       "      <td>59.000000</td>\n",
       "      <td>57.750000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>66.00000</td>\n",
       "      <td>70.000000</td>\n",
       "      <td>69.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>77.00000</td>\n",
       "      <td>79.000000</td>\n",
       "      <td>79.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>100.00000</td>\n",
       "      <td>100.000000</td>\n",
       "      <td>100.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       math score  reading score  writing score\n",
       "count  1000.00000    1000.000000    1000.000000\n",
       "mean     66.08900      69.169000      68.054000\n",
       "std      15.16308      14.600192      15.195657\n",
       "min       0.00000      17.000000      10.000000\n",
       "25%      57.00000      59.000000      57.750000\n",
       "50%      66.00000      70.000000      69.000000\n",
       "75%      77.00000      79.000000      79.000000\n",
       "max     100.00000     100.000000     100.000000"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "_cell_guid": "200d99af-060d-47f2-bcfb-ae1d686071cc",
    "_uuid": "491967b8-1c2b-428e-bae3-7184364e1cfa",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-01-05T20:08:36.283787Z",
     "iopub.status.busy": "2022-01-05T20:08:36.283547Z",
     "iopub.status.idle": "2022-01-05T20:08:36.293077Z",
     "shell.execute_reply": "2022-01-05T20:08:36.292413Z",
     "shell.execute_reply.started": "2022-01-05T20:08:36.283744Z"
    },
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "gender                         0\n",
       "race/ethnicity                 0\n",
       "parental level of education    0\n",
       "lunch                          0\n",
       "test preparation course        0\n",
       "math score                     0\n",
       "reading score                  0\n",
       "writing score                  0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T20:19:33.204927Z",
     "iopub.status.busy": "2022-01-05T20:19:33.204604Z",
     "iopub.status.idle": "2022-01-05T20:19:33.334982Z",
     "shell.execute_reply": "2022-01-05T20:19:33.333706Z",
     "shell.execute_reply.started": "2022-01-05T20:19:33.204887Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>race/ethnicity</th>\n",
       "      <th>parental level of education</th>\n",
       "      <th>lunch</th>\n",
       "      <th>test preparation course</th>\n",
       "      <th>math score</th>\n",
       "      <th>reading score</th>\n",
       "      <th>writing score</th>\n",
       "      <th>Total marks</th>\n",
       "      <th>Percentage</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>female</td>\n",
       "      <td>group B</td>\n",
       "      <td>bachelor's degree</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>72</td>\n",
       "      <td>72</td>\n",
       "      <td>74</td>\n",
       "      <td>218</td>\n",
       "      <td>72.666667</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>female</td>\n",
       "      <td>group C</td>\n",
       "      <td>some college</td>\n",
       "      <td>standard</td>\n",
       "      <td>completed</td>\n",
       "      <td>69</td>\n",
       "      <td>90</td>\n",
       "      <td>88</td>\n",
       "      <td>247</td>\n",
       "      <td>82.333333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>female</td>\n",
       "      <td>group B</td>\n",
       "      <td>master's degree</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>90</td>\n",
       "      <td>95</td>\n",
       "      <td>93</td>\n",
       "      <td>278</td>\n",
       "      <td>92.666667</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>male</td>\n",
       "      <td>group A</td>\n",
       "      <td>associate's degree</td>\n",
       "      <td>free/reduced</td>\n",
       "      <td>none</td>\n",
       "      <td>47</td>\n",
       "      <td>57</td>\n",
       "      <td>44</td>\n",
       "      <td>148</td>\n",
       "      <td>49.333333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>male</td>\n",
       "      <td>group C</td>\n",
       "      <td>some college</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>76</td>\n",
       "      <td>78</td>\n",
       "      <td>75</td>\n",
       "      <td>229</td>\n",
       "      <td>76.333333</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   gender race/ethnicity    ...     Total marks Percentage\n",
       "0  female        group B    ...             218  72.666667\n",
       "1  female        group C    ...             247  82.333333\n",
       "2  female        group B    ...             278  92.666667\n",
       "3    male        group A    ...             148  49.333333\n",
       "4    male        group C    ...             229  76.333333\n",
       "\n",
       "[5 rows x 10 columns]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[\"Total marks\"] = data[\"math score\"] + data[\"reading score\"] + data[\"writing score\"]\n",
    "data[\"Percentage\"] = data[\"Total marks\"] / 3\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "_cell_guid": "3bb34779-c999-4ff6-975e-47a450fd7b22",
    "_uuid": "59b3cb4e-403c-4768-9ad0-76c85ca8e9da",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-01-05T20:20:36.756198Z",
     "iopub.status.busy": "2022-01-05T20:20:36.755836Z",
     "iopub.status.idle": "2022-01-05T20:20:36.803002Z",
     "shell.execute_reply": "2022-01-05T20:20:36.801657Z",
     "shell.execute_reply.started": "2022-01-05T20:20:36.756139Z"
    },
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>race/ethnicity</th>\n",
       "      <th>parental level of education</th>\n",
       "      <th>lunch</th>\n",
       "      <th>test preparation course</th>\n",
       "      <th>math score</th>\n",
       "      <th>reading score</th>\n",
       "      <th>writing score</th>\n",
       "      <th>Total marks</th>\n",
       "      <th>Percentage</th>\n",
       "      <th>Grade_math</th>\n",
       "      <th>Grade_reading</th>\n",
       "      <th>Grade_writing</th>\n",
       "      <th>Overall_grade</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>female</td>\n",
       "      <td>group B</td>\n",
       "      <td>bachelor's degree</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>72</td>\n",
       "      <td>72</td>\n",
       "      <td>74</td>\n",
       "      <td>218</td>\n",
       "      <td>72.666667</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>female</td>\n",
       "      <td>group C</td>\n",
       "      <td>some college</td>\n",
       "      <td>standard</td>\n",
       "      <td>completed</td>\n",
       "      <td>69</td>\n",
       "      <td>90</td>\n",
       "      <td>88</td>\n",
       "      <td>247</td>\n",
       "      <td>82.333333</td>\n",
       "      <td>D</td>\n",
       "      <td>A</td>\n",
       "      <td>B</td>\n",
       "      <td>B</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>female</td>\n",
       "      <td>group B</td>\n",
       "      <td>master's degree</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>90</td>\n",
       "      <td>95</td>\n",
       "      <td>93</td>\n",
       "      <td>278</td>\n",
       "      <td>92.666667</td>\n",
       "      <td>A</td>\n",
       "      <td>A</td>\n",
       "      <td>A</td>\n",
       "      <td>A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>male</td>\n",
       "      <td>group A</td>\n",
       "      <td>associate's degree</td>\n",
       "      <td>free/reduced</td>\n",
       "      <td>none</td>\n",
       "      <td>47</td>\n",
       "      <td>57</td>\n",
       "      <td>44</td>\n",
       "      <td>148</td>\n",
       "      <td>49.333333</td>\n",
       "      <td>F</td>\n",
       "      <td>E</td>\n",
       "      <td>F</td>\n",
       "      <td>F</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>male</td>\n",
       "      <td>group C</td>\n",
       "      <td>some college</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>76</td>\n",
       "      <td>78</td>\n",
       "      <td>75</td>\n",
       "      <td>229</td>\n",
       "      <td>76.333333</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   gender race/ethnicity      ...      Grade_writing Overall_grade\n",
       "0  female        group B      ...                  C             C\n",
       "1  female        group C      ...                  B             B\n",
       "2  female        group B      ...                  A             A\n",
       "3    male        group A      ...                  F             F\n",
       "4    male        group C      ...                  C             C\n",
       "\n",
       "[5 rows x 14 columns]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def Grade(marks):\n",
    "    if marks >= 90:\n",
    "        grade = 'A'\n",
    "    elif marks >= 80:\n",
    "        grade = 'B'\n",
    "    elif marks >= 70:\n",
    "        grade = 'C'\n",
    "    elif marks >= 60:\n",
    "        grade = 'D'\n",
    "    elif marks >= 50:\n",
    "        grade = 'E'\n",
    "    else:\n",
    "        grade = 'F'\n",
    "    return grade\n",
    "        \n",
    "        \n",
    "data[\"Grade_math\"] = data[\"math score\"].apply(lambda s: Grade(s))\n",
    "data[\"Grade_reading\"] = data[\"reading score\"].apply(lambda s: Grade(s))\n",
    "data[\"Grade_writing\"] = data[\"writing score\"].apply(lambda s: Grade(s))\n",
    "data[\"Overall_grade\"] = data[\"Percentage\"].apply(lambda s: Grade(s))\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T20:21:16.761437Z",
     "iopub.status.busy": "2022-01-05T20:21:16.761086Z",
     "iopub.status.idle": "2022-01-05T20:21:16.771053Z",
     "shell.execute_reply": "2022-01-05T20:21:16.769725Z",
     "shell.execute_reply.started": "2022-01-05T20:21:16.761389Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "D    268\n",
       "C    216\n",
       "E    188\n",
       "F    135\n",
       "B    135\n",
       "A     58\n",
       "Name: Grade_math, dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.Grade_math.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T20:22:33.808639Z",
     "iopub.status.busy": "2022-01-05T20:22:33.808256Z",
     "iopub.status.idle": "2022-01-05T20:22:34.063060Z",
     "shell.execute_reply": "2022-01-05T20:22:34.062371Z",
     "shell.execute_reply.started": "2022-01-05T20:22:33.808578Z"
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "order_grade = [\"A\",\"B\",\"C\",\"D\",\"E\",\"F\"]\n",
    "sns.countplot(x = \"Grade_math\", data = data, order = order_grade, palette = \"GnBu_d\")\n",
    "_ = plt.xlabel(\"Grades in Mathe\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T20:24:39.600973Z",
     "iopub.status.busy": "2022-01-05T20:24:39.600347Z",
     "iopub.status.idle": "2022-01-05T20:24:39.611073Z",
     "shell.execute_reply": "2022-01-05T20:24:39.609956Z",
     "shell.execute_reply.started": "2022-01-05T20:24:39.600924Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "C    264\n",
       "D    233\n",
       "B    170\n",
       "E    164\n",
       "F     90\n",
       "A     79\n",
       "Name: Grade_reading, dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.Grade_reading.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T20:25:23.734614Z",
     "iopub.status.busy": "2022-01-05T20:25:23.734225Z",
     "iopub.status.idle": "2022-01-05T20:25:23.973285Z",
     "shell.execute_reply": "2022-01-05T20:25:23.971410Z",
     "shell.execute_reply.started": "2022-01-05T20:25:23.734555Z"
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x= \"Grade_reading\",data = data, order = order_grade, palette = \"GnBu_d\")\n",
    "_ = plt.xlabel(\"Grades in reading\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T20:38:28.701364Z",
     "iopub.status.busy": "2022-01-05T20:38:28.701000Z",
     "iopub.status.idle": "2022-01-05T20:38:28.935834Z",
     "shell.execute_reply": "2022-01-05T20:38:28.934495Z",
     "shell.execute_reply.started": "2022-01-05T20:38:28.701311Z"
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x = 'Grade_writing', order = order_grade, data = data, palette =\"GnBu_d\")\n",
    "_ = plt.xlabel(\"writing score\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T20:27:14.871371Z",
     "iopub.status.busy": "2022-01-05T20:27:14.870978Z",
     "iopub.status.idle": "2022-01-05T20:27:14.881980Z",
     "shell.execute_reply": "2022-01-05T20:27:14.880940Z",
     "shell.execute_reply.started": "2022-01-05T20:27:14.871306Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "C    261\n",
       "D    256\n",
       "E    182\n",
       "B    146\n",
       "F    103\n",
       "A     52\n",
       "Name: Overall_grade, dtype: int64"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.Overall_grade.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T20:28:02.674301Z",
     "iopub.status.busy": "2022-01-05T20:28:02.673741Z",
     "iopub.status.idle": "2022-01-05T20:28:02.894453Z",
     "shell.execute_reply": "2022-01-05T20:28:02.893195Z",
     "shell.execute_reply.started": "2022-01-05T20:28:02.674210Z"
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x = 'Overall_grade', order = order_grade, data = data, palette =\"GnBu_d\")\n",
    "_ = plt.xlabel(\"Overall Grade\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T20:28:52.726464Z",
     "iopub.status.busy": "2022-01-05T20:28:52.726089Z",
     "iopub.status.idle": "2022-01-05T20:28:53.083236Z",
     "shell.execute_reply": "2022-01-05T20:28:53.081962Z",
     "shell.execute_reply.started": "2022-01-05T20:28:52.726410Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.FacetGrid at 0x7f114da35dd8>"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.relplot(x='reading score', y = 'writing score', data = data) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T20:29:36.109448Z",
     "iopub.status.busy": "2022-01-05T20:29:36.108726Z",
     "iopub.status.idle": "2022-01-05T20:29:36.446916Z",
     "shell.execute_reply": "2022-01-05T20:29:36.445830Z",
     "shell.execute_reply.started": "2022-01-05T20:29:36.109394Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.FacetGrid at 0x7f114d9cc358>"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.relplot(x='writing score', y = 'reading score', data = data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T20:30:07.019921Z",
     "iopub.status.busy": "2022-01-05T20:30:07.019169Z",
     "iopub.status.idle": "2022-01-05T20:30:07.026013Z",
     "shell.execute_reply": "2022-01-05T20:30:07.025323Z",
     "shell.execute_reply.started": "2022-01-05T20:30:07.019850Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9545980771462476\n"
     ]
    }
   ],
   "source": [
    "r = np.corrcoef(data[\"reading score\"], data[\"writing score\"])[0, 1]\n",
    "print(r)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T20:30:39.942839Z",
     "iopub.status.busy": "2022-01-05T20:30:39.942482Z",
     "iopub.status.idle": "2022-01-05T20:30:39.953814Z",
     "shell.execute_reply": "2022-01-05T20:30:39.952815Z",
     "shell.execute_reply.started": "2022-01-05T20:30:39.942786Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "group C    319\n",
       "group D    262\n",
       "group B    190\n",
       "group E    140\n",
       "group A     89\n",
       "Name: race/ethnicity, dtype: int64"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[\"race/ethnicity\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T20:34:25.293523Z",
     "iopub.status.busy": "2022-01-05T20:34:25.292927Z",
     "iopub.status.idle": "2022-01-05T20:34:25.861486Z",
     "shell.execute_reply": "2022-01-05T20:34:25.860468Z",
     "shell.execute_reply.started": "2022-01-05T20:34:25.293460Z"
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.set(style = \"ticks\")\n",
    "order_race = [\"group A\",\"group B\", \"group C\", \"group D\", \"group E\"]\n",
    "sns.boxplot(x = \"Percentage\", y = \"race/ethnicity\", data = data, palette = \"vlag\", order = order_race)\n",
    "sns.swarmplot(x = \"Percentage\", y = \"race/ethnicity\", data = data, size = 2, color = \".3\", linewidth = 0, order = order_race)\n",
    "sns.despine(trim = True, left = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T20:39:04.416000Z",
     "iopub.status.busy": "2022-01-05T20:39:04.415487Z",
     "iopub.status.idle": "2022-01-05T20:39:04.425555Z",
     "shell.execute_reply": "2022-01-05T20:39:04.424328Z",
     "shell.execute_reply.started": "2022-01-05T20:39:04.415956Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "standard        645\n",
       "free/reduced    355\n",
       "Name: lunch, dtype: int64"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[\"lunch\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T20:40:21.324174Z",
     "iopub.status.busy": "2022-01-05T20:40:21.323477Z",
     "iopub.status.idle": "2022-01-05T20:40:21.685567Z",
     "shell.execute_reply": "2022-01-05T20:40:21.684349Z",
     "shell.execute_reply.started": "2022-01-05T20:40:21.324101Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x7f114d8d8080>"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x = \"lunch\", data = data, hue = \"Overall_grade\", hue_order = [\"A\",\"B\",\"C\",\"D\",\"E\",\"F\"], palette = \"GnBu_d\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T20:40:50.314221Z",
     "iopub.status.busy": "2022-01-05T20:40:50.313490Z",
     "iopub.status.idle": "2022-01-05T20:40:50.324518Z",
     "shell.execute_reply": "2022-01-05T20:40:50.323556Z",
     "shell.execute_reply.started": "2022-01-05T20:40:50.314140Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "none         642\n",
       "completed    358\n",
       "Name: test preparation course, dtype: int64"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[\"test preparation course\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T20:41:30.549040Z",
     "iopub.status.busy": "2022-01-05T20:41:30.548661Z",
     "iopub.status.idle": "2022-01-05T20:41:30.905815Z",
     "shell.execute_reply": "2022-01-05T20:41:30.904619Z",
     "shell.execute_reply.started": "2022-01-05T20:41:30.548978Z"
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x = \"test preparation course\", hue = \"Overall_grade\",data = data, hue_order = order_grade, palette = 'GnBu_d')\n",
    "_ = plt.legend()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T20:42:00.356444Z",
     "iopub.status.busy": "2022-01-05T20:42:00.356069Z",
     "iopub.status.idle": "2022-01-05T20:42:00.365730Z",
     "shell.execute_reply": "2022-01-05T20:42:00.365082Z",
     "shell.execute_reply.started": "2022-01-05T20:42:00.356381Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "some college          226\n",
       "associate's degree    222\n",
       "high school           196\n",
       "some high school      179\n",
       "bachelor's degree     118\n",
       "master's degree        59\n",
       "Name: parental level of education, dtype: int64"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[\"parental level of education\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T20:42:40.124390Z",
     "iopub.status.busy": "2022-01-05T20:42:40.123701Z",
     "iopub.status.idle": "2022-01-05T20:42:40.590701Z",
     "shell.execute_reply": "2022-01-05T20:42:40.589816Z",
     "shell.execute_reply.started": "2022-01-05T20:42:40.124314Z"
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "order_edu = ['some high school','high school',\"associate's degree\",\"some college\",\"bachelor's degree\",\"master's degree\"]\n",
    "p = sns.countplot(x='parental level of education', hue='Overall_grade',data=data, order= order_edu, hue_order = order_grade, palette = 'Paired')\n",
    "_ = plt.xlabel('Parents level of education')\n",
    "_ = plt.setp(p.get_xticklabels(), rotation = 60)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T20:51:48.393946Z",
     "iopub.status.busy": "2022-01-05T20:51:48.393618Z",
     "iopub.status.idle": "2022-01-05T20:51:49.101067Z",
     "shell.execute_reply": "2022-01-05T20:51:49.099692Z",
     "shell.execute_reply.started": "2022-01-05T20:51:48.393892Z"
    }
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/conda/lib/python3.6/site-packages/scipy/stats/stats.py:1713: FutureWarning: Using a non-tuple sequence for multidimensional indexing is deprecated; use `arr[tuple(seq)]` instead of `arr[seq]`. In the future this will be interpreted as an array index, `arr[np.array(seq)]`, which will result either in an error or a different result.\n",
      "  return np.add.reduce(sorted[indexer] * weights, axis=axis) / sumval\n"
     ]
    },
    {
     "data": {
      "image/png": "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IYQQQgghhBBeRRq6QgghhBBCCCG8ijR0hRBCCCGEEEJ4FWnoCiGEEEIIIYTwKtLQFR5hzpw5fP3112rHEEIIIYQQQngAaegKzVm9ejUvvPCC2jGEEGJArFy5knXr1gFd+yzef//9KicSQoirl5GRQXl5+SXvX7hwIfv37x/EREJ0MaodQAhP43Q6MRrlv44Q4trdfvvt3H777WrHEEKIq3bkyJHuv69evZrY2Fj+8z//s/t7mzZtUiOWENKjK/rHnDlz+Pvf/85tt93G5MmTeeKJJ6irq+PBBx8kIyODf//3f6epqan7+FWrVjFr1iwyMzO5++67KSgoAOD9999nw4YNvP7662RkZPDjH/+4+zGnTp3itttuIzMzk8ceewy73X7RLKWlpdxzzz1kZmYyffp0Hnvsse77CgoKuO+++5g2bRrXX389r7zyCgCdnZ08//zz3HDDDdxwww08//zzdHZ2ArB//35mz57Nq6++yqxZs3j88ccB2L59O4sXL2bq1Kncdddd5Obm9u8vVQihOqfTqXYETVIUBbfbrXYMIYSKvL0+evvPNxRIQ1f0my1btvDGG2+wefNmtm/fzkMPPcTPf/5z9u3bh9vt5n/+53+6j509ezabN29m7969jB07ll/+8pcALF++nNtuu40HHniAI0eOdDdEAf71r3/x97//nS+//JK8vDw++uiji+b405/+xKxZszh48CA7d+7knnvuAaC1tZX77ruPG2+8kV27drFlyxZmzpwJwF//+ldycnJYv349n376KceOHePll1/ufs66ujqamprYvn07zz77LCdPnuSJJ57gN7/5Dfv372f58uX85Cc/6W4cCyE815w5c3j11Ve7L9w5nU6qq6t59NFHmTFjBnPmzOHNN9/sPv7o0aMsX76cqVOncsMNN/Cb3/ymRy3Ys2cPCxYsIDMzk9/85jcoitJ930cffcQPf/jD7q/T0tJ49913mTdvHlOnTuWZZ57pPt7lcvG73/2O6dOnM2fOHN566y3S0tIueTL26quvcuONN5KRkcH8+fPZu3dv9/O88sorzJ07l4yMDO644w4sFgsAWVlZfP/73yczM5Pvf//7ZGVldT/fypUreeGFF7jrrruYNGkS5eXltLS08MQTT3DDDTdw44038sILL+ByufrhVRBCDJZ//vOfPToW5s2bx6pVq7q/vummmzh1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\n",
      "text/plain": [
       "<Figure size 1152x360 with 3 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize =(16,5))\n",
    "plt.subplot(1,3,1)\n",
    "sns.distplot(data[\"math score\"])\n",
    "plt.subplot(1,3,2)\n",
    "sns.distplot(data[\"reading score\"])\n",
    "plt.subplot(1,3,3)\n",
    "sns.distplot(data[\"writing score\"])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T20:45:00.043514Z",
     "iopub.status.busy": "2022-01-05T20:45:00.043057Z",
     "iopub.status.idle": "2022-01-05T20:45:00.048627Z",
     "shell.execute_reply": "2022-01-05T20:45:00.047604Z",
     "shell.execute_reply.started": "2022-01-05T20:45:00.043440Z"
    }
   },
   "source": [
    "# Conclusion \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T21:12:31.698480Z",
     "iopub.status.busy": "2022-01-05T21:12:31.698073Z",
     "iopub.status.idle": "2022-01-05T21:12:32.309192Z",
     "shell.execute_reply": "2022-01-05T21:12:32.308359Z",
     "shell.execute_reply.started": "2022-01-05T21:12:31.698416Z"
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "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//7v/66RI0fqi1/8okpKSvTWW2/p/vvv10svvaRHHnkk4mNcddVVWrNmjY466igdf/zxKikpGdTv0tLSovPOO085OTk65ZRT1NzcrOeee06XXHKJ/vKXv+jmm29Wc3OzjjnmGAUCAS1fvlxXX321xo8fH15PN5Tn4+GHH9Y//vEPLVq0SPPmzdO//vUvPffcc1q3bp2eeuopZWVlDWrciD/iJ/GT+DmwpqYmffWrX9WoUaN04oknyuPxhH+2paVFF154oT7++GPNmjVLZ511lmzb1uuvv65rrrlG69ev19VXXx2+r+bmZt1666066KCDdNhhh6m4uFh1dXV66aWX9K1vfUs//elPdfbZZ/d6/L/97W+6+uqrlZmZqZNPPlljxozRO++8o3PPPXdY638Hc/yHPPvss7rmmmuUnZ2tk046SWPGjNF7772nc889V/vtt9+QHxuDQ1wmLhOXI1uwYIGeeeYZbdiwITy7oKqqSjU1NZKkVatW6fLLLw/fftWqVZKkhQsX9rmvW2+9VW+//baOPvpoHX300fL5fBEfMz8/v9/fv6ysbMDxhrz88stasWKFjjzySJ177rnasGGDXnnlFa1Zs0bPPvusiouLw7fdsGGDzjvvvHBeHiqEXHHFFTrqqKMG9XhJyaSQjz76yMyaNctUVFSYa6+91vz973831dXVA/7MY489ZsrLy81jjz0W8frrr7/elJeXmy1btvS5btWqVaa8vNzcdddd4cts2zaLFy825eXl5v/9v//X6/YPPvigKS8vN+Xl5WbVqlXhy5uamszcuXPN/Pnzzfr163v9zCeffGLmzJljTj/99IjjOvroo83WrVvDl/v9fnP++eeb8vJy88EHH/T6mWOPPdYce+yxEX/PK664wpSXl5u1a9f2ua6hoSHiz+xpy5Ytpry8POJjPPnkk6a8vNwsWLDAdHZ29rou9BpcfvnlpqOjo9d1d911lykvLzcPPvjgsMZ6wQUXmPLy8ojj7e+1j/Q87e04GUh/Y6iurjazZs0yBx10kPnss896XfeTn/zElJeXmx/96EcR7+tLX/rSoF+XkNCx9+Mf/9hYlhW+/IknnjDl5eVm3rx55tJLL+31+qxevdqUl5eb73znO73ua2/PR+h1O+igg8y6det6Xff973/flJeXm2effXZI40d8ET+Jn8TP/oWOvR/84AfG7/f3uT50TP3ud7/rdXlnZ6e5+OKLTUVFhfn444/Dl3d1dZlt27b1uZ+WlhZzyimnmHnz5vV6PXft2mXmz59vZs6caf71r3/1+plbb701PL6e77XQMXX99ddHHOtgj//W1lYzd+5cM2vWrD7HzS9+8YuIj43YIC4Tl4nLkf31r3815eXl5qGHHgpf9sgjj5jy8nLz9a9/3cyaNcu0t7eHr/vyl79sZs+ebbq6usKXhY65I444wmzevLnPY0R6Pwz0+4cM9Hzvv//+5o033uh13S9/+cuInx//9m//ZsrLy82f//znXpe//PLL4ffdcF4/p6XUsoiZM2fq5z//uUaPHq2nn35aV155pRYtWqRDDz1Ul19+uf7xj3/EfQzvvvuuKisrNW/ePB1//PG9rrvgggsirsN58skn1dLSoquuukozZszodV15ebnOPvtsffzxxxGnXV1++eWaMGFC+P8ZGRk688wzJUn/+te/hjz+7OzsPpf1rKINRktLi+6++27dfffduv3223XZZZfp+uuvV2Zmpm655ZY+j7F06VJlZGTotttu04gRI3pd953vfEeFhYV65pln4jJWJz399NPy+/264IIL+qzpuvrqq5WTk6Onnnoq4vS57373u8P6XUeOHKnrrrtOXu/nb+1TTz1VGRkZam5u1k033dTreZ07d67Kysq0du3aIT+WFHn6Xuhs3Jo1a4Z1n4gP4ifxk/g5sMzMTF1//fXhs40hO3fu1NNPP60DDjhA3/zmN3tdl52drR/84AcyxvR6HbKyslRaWtrnMfLy8nTWWWepubm5V4xcsWKFmpqa9KUvfUkHHnhgr5+58sorh9W0cbDH/4oVK9TS0qJTTz21zyyFb3/721GdEcfAiMvEZeJyZKEZCCtXrgxftnLlSo0ePVpLliyR3+/XO++8IykYo9etW6dDDjkk4ozZb3zjG5o0adKgHzsaJ598cp/ZE+ecc46k3nnxtm3btGrVKk2ZMkXnnntur9sfffTROuyww+I/2DhJqWURUvBFO+GEE/Tmm2/qnXfe0dq1a/XOO+/oxRdf1IsvvqjTTz9d//3f/y2PxxOXx//4448lSfPmzetznc/n0yGHHKLNmzf3uvz999+XJK1bty7iOrfQdLgNGzb0CdIHHHBAn9uPHz9eUnDa5WCdeuqpeuGFF3TOOefopJNO0oIFC3TwwQdHTH72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jW98Q3PnzlVWVpb2228/LVq0SD/96U9VW1urgw8+WGVlZcrMzNRHH32kVatWqaysTKecckpUjy0FA+Jxxx2nFStW6P/+7//C3U+/8pWv6KOPPtLDDz+sE044QUcccYTGjx+v5uZmVVdXa/Xq1TrzzDN1yy23SNKQxnrWWWfpD3/4g+677z6tW7dO++yzjzZt2qTXXntNJ5xwgv7+978Paux7O06GY+LEibrhhht0yy236IwzztBJJ52k4uJirV69Wu+9956mT5+ua6+9dlj3HW/xeD7gLOLnwIifxM+B3HzzzaqqqtJdd92lp59+WgcffLBGjx6tHTt2aMOGDVqzZo1+9atfhZvmXnjhhXr99dd1/vnn66STTlJeXp4+/PBDvfPOO1q8eHGf5zYnJ0e33HKLrr76an3ta1/TySefrDFjxuidd97R+vXrNW/evIhnlmMhNzdXN998s6677jqde+65OumkkzRmzBi99957WrdunebPn6+33norYtMxRIe4PDDiMnF5wYIF+vTTTyWpV3EhKytLBx98cLjfwp47NERj4cKF+tvf/qYrr7xSRx99tLKzszVhwgSdfvrpMXsMSfrJT36i8847T//xH/+hV199VRUVFdqyZYteeOGF8HGXinE3pYoLF198saZOnao33nhDn3zyiV5//XV1d3ersLBQ8+fP15e+9CWdeuqpvdbWFBQU6K677tKvf/1rPfHEE+HmMqeddpry8vKUnZ2tBx98UD/72c/0xhtvaM2aNdp33311++23q6CgoE8QloIdPP/85z/rjjvuCE9l+sIXvqA//elPev311/sEYSl4oD799NN64IEH9Prrr+vtt99WZmamxo4dqwULFmjx4sVRPz/f/va31dLSopdeeknvvvuuLMvSGWecoUWLFunSSy/Viy++qA8//FArV66Ux+PRhAkTdNlll+nCCy8MT8OK1lVXXaV//OMf+s1vfqMzzjgjvO3OT37yEx111FF69NFH9cYbb6i1tVUFBQUaP368LrnkEp122mnh+xjKWEtKSvTQQw/p5z//uVavXq3Vq1frgAMO0AMPPKDq6upBB+G9HSfD9bWvfU1TpkzRAw88oBdeeEEdHR3h3/myyy5L2i2+4vV8wDnEz4ERP4mfA8nNzdWf/vQnLVu2TMuXL9cLL7ygrq4ujR49WlOmTNENN9zQa+uwo446Sr/97W9177336rnnnpPP59Ps2bO1dOlSbdmyJeJz+8UvflF5eXm655579PzzzysrK0tz587Vo48+qvvvvz9uxQUp+FoVFBSEx9vzsX/+85+HnwPEFnF5YMRl4vLChQu1dOlSeTyePsvMFi5cGN6eMlIPiOE6++yzVVNTo2effVa///3vFQgENH/+/JgXF2bMmKFHH31Ud9xxh1atWqVVq1apoqJC99xzjzZs2KAVK1akZNz1mJ4LuQAAAAAF1xwff/zx8vv9EZdzAABi75prrtHy5cv1/PPPa/r06U4PZ0hSb64FAAAAYqalpUUdHR29LjPG6N5771VNTU3ctkEEALeybTu8w0ZPK1eu1PPPP68ZM2akXGFBSrFlEQAAAIit999/X1dffbUOP/xwlZWVhbfLW7t2rcaPH68rr7zS6SECQFrx+/065phjdOihh2r69Ony+Xz67LPP9M9//lOZmZm6+eabnR7isLAsAgAAwMW2bNmi//mf/9F7772nxsZGBQIBlZaW6phjjtFll10WbgYHAIgNy7J02223adWqVdq+fbs6OztVVFSkuXPn6lvf+lZ4m9hUQ3EBAAAAAABEhZ4LAAAAAAAgKhQXAAAAAABAVCguAAAAAACAqFBcAAAAAAAAUaG4AAAAAAAAokJxAQAAAAAARCXD6QEAGB6/36/q6mp1dnY6PZSE8/l8Kiws1OjRo+X1UiMF4Aw3x2FJGjFihCZOnKjMzEynhwLAxdwci5MtJ/YYY4zTgwAwdJWVlcrLy1NJSYk8Ho/Tw0kYY4z8fr9qa2tljNHkyZOdHhIAl3JrHJaCsbihoUGtra2aNm2a08MB4GJujcXJmBM7X94AMCydnZ2uC6KS5PF4lJWVpbKyMrW1tTk9HAAu5tY4LAVjcUlJiSvPFAJILm6NxcmYE1NcAFKY24JoT8kw9QsA3ByH3fy7A0gubo5HyZQTJ89IAAAAAABASqK4AKSLeLVPoS0LAAwaoRgAHEYgdgy7RQDpwuOR2ptjf7+jCmJ/nwCQpjweqTMQ+/sdQcYGAINDTuwYPqoAxERFRYUuv/xyrVixQp2dnfr+97+vxYsXS5KuueYaVVZWyu/3a/LkybrttttUUFCgjRs36oYbblBHR4ds29YZZ5yhSy65RC+++KLuvPNOeb1eWZalH//4xzr00EMd/g0BILkRhwHAeW6OxRQXAMSM1+vVU089pY0bN+q8887T3LlzVVJSoptuuknFxcWSpDvuuEP333+/rr32Wj388MNatGiRLr30UklSc3OwynzXXXfplltu0UEHHSTLstTR0eHY7wQAqYQ4DADOc2ssprgAIGbOPvtsSdL06dM1c+ZMvf/++zruuOP01FNP6ZlnnpHf71d7e7umTp0qSZo3b55+8YtfqKOjQ4ceeqgWLFggSVqwYIH+67/+SyeeeKKOOuoolZeXO/UrAUBKIQ4DgPPcGotp6Aggrt5++2098sgj+v3vf69nnnlG3/ve99Td3S1JWrx4sf785z9r8uTJuv/++/WDH/xAknTjjTfqP//zP5WZmanvfve7WrZsmZO/AgCkNOIwADjPDbGY4gKAmHnsscckSZs2bdLHH3+sOXPmqKWlRbm5uSosLFR3d3f4NpJUVVWlMWPG6Mwzz9Tll1+uNWvWSJI2btyoiooKXXjhhTrttNPClwMABkYcBgDnuTUWsywCSBfGxKeLrTHBrruDYFmWTj/9dHV0dOiWW25RSUmJjjzySD399NNavHixioqKNHfu3HBgfP755/XMM88oMzNTHo9HN954oyTp9ttvV1VVlXw+n/Lz83XrrbfG/vcCgDgwJj47Oww2FBOHAbgeObFjPMawYSeQitauXav999/f6WGEVVRU6N1331VOTk7CHjPZngMA7pJsMYg4DMCNki0OuTkWsywCAAAAAABEhWURAGLik08+cXoIAOBqxGEAcJ6bYzEzFwAAAAAAQFQoLgAAAAAAgKhQXAAAAAAAAFGhuAAAAAAAAKJCcQFIE8ayUup+ASAd+S07pe4XANKN8Xen1P2mE3aLANKEx+eT9eLSmN+v7/h/G9TtXnzxRd1+++3Kzs7Wr371K02fPr3PbdasWaMHH3xQt99+u6qrq3XWWWfpzTffjPWQAcAxmT6vLn9ibczv99dnDG7/cmIxALfzZGYp8J1TYn6/Gb95dlC3c3McprgAICYeffRRXXXVVTrppJP6vc2BBx6o22+/PYGjAgB3IRYDgLPcHIcpLgCI2m233aZ33nlHlZWVevjhhzV27FhVVlbK7/dr8uTJuu2221RQUKA333xTP/vZz/T44487PWQASDvEYgBwltvjMMUFAFG78cYbtXbtWl188cU69thj1djYqOLiYknSHXfcofvvv1/XXnutw6MEgPRGLAYAZ7k9DlNcABBzTz31lJ555hn5/X61t7dr6tSpTg8JAFyHWAwAznJbHKa4ACCm3n77bT3yyCN69NFHVVxcrGeeeUbLli1zelgA4CrEYgBwlhvjMFtRAoiplpYW5ebmqrCwUN3d3XrsscecHhIAuA6xGACc5cY4zMwFIE0Yyxr0tpFDvV+Pzzfo2x955JF6+umntXjxYhUVFWnu3Llas2ZNzMcFAMnIb9mD3jZyqPeb6Rv8OSFiMQC3Mv7uQW8bOdT79WRmDfr2bozDHmOMcXoQAIZu7dq12n//2CewqYTnAICTiEE8BwCcRxxKnudQ4c/JAAAgAElEQVSAZREAAAAAACAqFBcAAAAAAEBUKC4AKczNq5ps23Z6CADg6jjs5t8dQHJxczxKppyY4gKQokaMGKGGhgbXBVNjjLq7u7V161bl5OQ4PRwALubWOCwFY3FDQ4NGjBjh9FAAuJxbY3Ey5sQ0dARSlN/vV3V1tTo7O50eSsJlZGSooKBAo0ePltdLjRSAM9wch6VgQj9x4kRlZmY6PRQALubmWJxsOTHFBQAAAAAAEBXnyxsAAAAAACClUVwAAAAAAABRobgAAAAAAACiQnEBAAAAAABEheICAAAAAACICsUFAAAAAAAQFYoLAAAAAAAgKhQXAAAAAABAVCguAAAAAACAqFBcAAAAAAAAUaG4AAAAAAAAokJxAQAAAAAARIXiAgAAAAAAiArFBQAAAAAAEBWKCwAAAAAAICoUFwAAAAAAQFQoLgAAAAAAgKhQXAAAAAAAAFGhuAAAAAAAAKJCcQEAAAAAAESF4gIAAAAAAIgKxQUAAAAAABAVigsAAAAAACAqGU4PAC5jTM//7HGlZ4//7vF/AEDUzJ6hdy8IxQAQB+FgbPR5DtxPbkwgRoqguIDYM0a9AqUxkm1Jxv78uvC/e/B41CuIeryS1yt5fL2DKgEWAPZqzxBrdl/W8+9Itw+FWE/o3yY4zXHP0EsoBoBB6BmMjR38Y5vP/x3Om3vqmQ+HcmJf8G9yYiQxjzFDPYcBRBA6jIwtWYFgMSFUUIiVUGD1ZQT/aHfW62F1DwD0/DS3ze7cdfe/YyVUcPB6+hYcyHEBQHvkxJZkB2KfE3t9n/8hJ0YSobiA4el52Fj+YEHBCqhv5TWOPB7JmyFlZAb/Dl0GAC4RzmElWfbnBYVE8u4uNvgoNABwo145cWB3XuxP8CA8wSJDRlaw4CARiOEIigsYmtDhYvmlQHewEpssfJkEVQBpLxkKCv3xKFhoyNh98owwDCBthYJxYHcxwQ44O56efJmcfIMjKC5g73pO7wp0B/8kNU8woGZmB/9NQAWQBsK1XRMsKiT7h3doNoOXfmQA0kU4JzZSoCtFcuIsKTNL5MRIBIoL6F/o0LADUndnbNeKJYpvd5HBw2k0AKkpfHLMDhYWUo1Hks/7+bIJwjCAlBOu7gaCRYVkmrk7WOTESACKC+irZwD1p2hRYU9en5Q5YnenXYIpgOQXCsV+O7ZNGZ2UQZEBQCohJwaGhOICejMmvQLonrw+KWtk3618ACBJpPpMhcGgyAAgqYVn71pSd0ea5sQZUtYIcmLEFMUFBJnd++12d6TmVK+h8mUGAyrrzwAkiZ49FQJpmMdGEioyEIYBJA1jgrmwv5OcGBgiigtuF55325kCTWniIDNbysgO/puACsAhxgSXPvhdUlToySMp0xf8mzAMwDGhnLi7w4GtJJMAOTFigOKCmxkTDJ7dnUr+vuNx5PFKWaMkL9PCACRWOvZVGC4fW1gCcIoxwQbmXR1yfU6cPYqlEhg2igtuZIwkEwygybQnr9MysoINbiQCKoC4c/Nshf4wiwFAQoVy4u6OYM8xBJETY5goLrgNldmBUbEFEGfMVti70CwGwjCAuAk1Me9ud3okyYmcGMNAccEt3L6ObKhC684IpgBiyJjgn25mK+yVR1KWb/e/CcUAYoWceGgyRwRnMhCIMQgUF9wgtBNEV3t6bqUTL76MYC8GiYAKIGrGuGsniFjJ9EpempgDiIVQhberjZx4KMiJMUgUF9JdeBkEU76GxeOVsnOCgZRgCmAYWAYRPZZJAIgaOXF0WCaBQaC4kM6MCW4v6e90eiSpL3uU5M0gmAIYkvDsW4suN9HyeoKzGCRCMYAhMkbyd0mBLqdHkvqyRgVnMhCIEQHFhXRlDGvJYi0jO9iLgWAKYBDorxB79GEAMGTkxLFHbzL0g+JCugm9nF1tkm05O5Z05MuUskYSTAEMiG0m4yuL7SoB7A05cXyFtqskEKMHigvpJLRXbydNauLKm7F7zRnBFEBfNG5MDBo9AugXOXFihBo9EoixG8WFdBHufrvr80ot4sfrCzZ6lAioAMLM7qKCRRhOiAxvsNkjYRhAWHiXtDZy4kQgJ0YPFBfSQSiIdraJlmEJ5PFKI3IkkdkCoLDgFAoMAMLCOfEup0fiLuTE2M3r9AAQJQoLzgl/eBkq44DLmd39FSgsJF6ooEMYBlyOwoJzen4XIRi7GsWFVGZMsEFN6AsuEs8YCgyAy4UKCzYhwDEUGACXo7DgPAoMEMWF1NVzPRmcZQzBFHCp0FIICgvOo8AAuBSFheRBgcH1KC6kolDzxk4KC0kjHExFMAVcgh4LyYcCA+AyFBaSDwUGV6O4kGpCW+t0sRQi6fDhBrgGhYXkFZpJQk4LpDlOtiWvnifd4CoUF1JJrz17yZqSElsfAWnPmGBRgcJC8vLbn3/vAJCuONmW1MiJXYniQqrpbAu+WZG8bEvqbieYAmnImOBZ8QBhOOl128GvHIRiIA0ZI3WRayU925K6O3idXITiQqowZnf1j4w2JVgByd9FMAXSiDHBL6t+wnDK6LaCfxOKgTQSKizYltMjwWBYfnJiF6G4kAqMkenuIIimmkBXMKASTIGUF3obdxOGUw6vGZBGwjlxwOmRYCjIiV2D4kKyM0Ym0C2P5Xd6JBiOUFGIYAqkPL6kpiaj4GtHGAZSnDEygS5y4lRFTuwKFBeSmTGSbcnj73R6JIhGqJkNwRRIScbs/nLq9EAwbEbBPhmEYSBFhXPiLqdHgmiQE6c9igvJKvTG62p3eiSIhS624wFSkTFSwDIUFtKAZdiiEkhJ4ZyYXCot8DqmNYoLyayrTZwrSxPGZgcJIMUEt5w0suRxeiiIET87SACpiS+k6cPY7CCRxiguJCNjdn8RpSV5WrECUqCbYAqkgODOEEYBm8JCuqF3BpBCjJHpIidOO5afnDhNUVxINrsbOMqiC25a8nfSzAZIEX6LwkK68tN/AUh+oabm7AyRnsiJ0xLFhWRijIyxaeCY7rrbxXIXIHkZ8/n0eaQn29DgEUhqxsjQ1Dz9dZETpxuKC0nGQwPH9Bdq1ElWCyQdY6SAbWTz9kx7lqFpOZDMPN3kxOmPnDjdUFxIFqwpcxfbkvxdBFMgiYT6LFiG5RBu0c1HLpB8wr3HyJFcwbakADlxuqC4kAxYU+ZOgS7JZl4ukEzos+A+9F8Akgi9x9zJ3xU8wUowTnkUF5xGnwV3Y8ofkBSCfRYMKz9dyDafL5EA4CxjDDmxW7E0PC1QXEgC9FlwMWMHu+WS1QKOMUayjZHNcgjXCrA8AnCcMYY+C25GTpwWKC44yRiZ0DQguFegm614AEcZ+W0KC27XTRgGnGOMTPfurQnhXuTEKY/iglOMkbFteQJdTo8EyYBKPeCI4HIICgsIbobG8gjAAbu3nfRa3U6PBMmAGd0pjeKCQ4zYYgc9GCN1d5DVAglkjGTZNttOIixgs+M6kGjBnLjD6WEgaZATpzKKC04ITf1iOQR6svySHSCYAgljFDB8DKI3PzNygcQxRsZPTow9WH6WR6QosqpEM0Y2U7/QHyr3QEIYQ58FRMbyCCBxbNuWN0BOjAiY4Z2SKC4kmJHk5Qsk+mMMnXKBOAsuhzAsh0C/2D0CiD9jbHn95MTohzGSv4ucOMVQXEgklkNgMALdHCNAXBlZLIfAXvhtclogboyR7e9mdwgMLMCueqmG7CqBjDEsh8Dg0MgGiAtjjPyWoWkf9so2wT+EYiD2bGPLx45pGAxy4pRCcSFBjG1LTP3CYNlWsJkNwRSIKcu2ZfPRh0Hyc8IMiDlj2/L6O50eBlIFOXFKIcNKBGNkWwF5rIDTI0Eq6eaDF4gl2xhZxuf0MJBiAiyPAGJnd04scmIMBTlxyqC4kAC2MUz9wjCwzy8QK8ZIActmOQSGzOKgAWLGkBNjWMiJUwXFhTgzti3jpxkJhol9foGYMMaWLWYtYHho7ghEz7Zt2eTEGC5y4pRAcSHOjDHy0cQR0WDrUiAqtm0rwL6TiALNHYEYICdGtMiJkx7FhTiyLUsepn4hWsbevT0lWS0wHMYYZi0gagFOtgLDZlkBiSaOiBY5cdKjuBBHxrbksfxODwPpgA9kYFgCAUsWhQXEgFGw/wI5LTB0xrbltWniiBjwc+I2mVFciBPLspj6hdjyd5LVAkNg20a2MWJFBGKF2QvA0FmWpQxyYsSMkQJd5MRJiuJCHNiWJTuwu+kIECuBbole98CgGWPLeDKcHgbSDFtTAoNn27bsQDc5MWKL2QtJi+JCHBgZZdosh0Ac+KnUAoNhWRZbTyIu2JoSGAJjlMlyCMQDM3qTEsWFGAv4/bL93Wyzg/hg9gIwOB6P5M10ehRIU2xNCexdIBBg60nEDzlxUqK4EGMer0eZhgot4qibSi0wEL/fr0CAWQuIH/p4AHvn8XiUQU6MeGJGb9KhuBBDXV1dMn62R0GcWX5RqQX65/V6Zbz0WkB8MXsB6F8wJ+aLH+KM2QtJh+JCDGVk+JTBujIkArMXgIg6u7oU4LQyEsA2pLRAfzJ85MRIEHLipEJxIUY6OzskP9UzJIjlJ5ACezDGKDMjgx0ikDDsHAH01dHezhllJA45cVKhuBADwYQ2Uz52iEAi0SUX6KW9vUMB+oYhgZi9APRmjFFWVpZ8zFpAIpETJw2KCzHQ1dkpT6Db6WHAbSw/HZiB3Ywxys7OkvH4nB4KXIbZC8Dn2pm1ACeQEycNigtRMsYoIzNTXmYtwAlUagFJUltbmyzjcXoYcCHbBMMwoRhuFyzyZjOTF86g90JSoLgQpV27djFrAc6xAlRq4Xq2bWvEiBHMWoBj/IRhQB3t7eTEcI5NTpwMKC5EwbIsjRw5Uj728IWTqNTC5Xbt2iWLtwAcZPT5DAbAjWzbVhazFuC07g4CscMoLkRh586dMoFuDmI4i0otXMy2bY0aNYodIuA4monCzdra2pi1AOfZVvAP380cQ3FhmCzLUn5enjKN5fRQACq1cK1du9qYtYCkYEQYhjvZth2cycsOEUgG/k6nR+BqFBeGqaG+XjIWZ4yRHEKVWsBFgrMWRjJrAUkjwNIIuNDOnY3BmbzsEIFkYPP9zEkUF4bBGKOcnBxliQMXSSTQRVYLV2lublbA5phH8uBwhNtYlqXcnFxm8iK5+MmJnUJxYRgaGxqUmeHjTDGSixUQZw3gFsYYjRo1Sh5vptNDAXoJ2OS0cI8dO2rlkeFMMZKL5Rc5sTMoLgyD1+tVlocDFkmISi1cor6+PrjG3emBAHugBwjcwrZtjcgeoSwPhQUkIXJiR1BcGKLm5mbl5uburogBSYZOzXABY4y8Xp+8GdlODwWIyKL3Alygvr5eubk5u2dOAkmGnNgRFBeGqLurSz5DEEUSY3tUpLna2lrl5eexvh1Ji20p4QZWICAfvRaQzMiJE47iwhC0t7erqKhIXmYtIJkFupweARBXXV3dMnx8IckxewHprKmpSWPGjCEnRnIjJ044srMhaG1pZjkEkp8xkh0gq0Vaampq0oQJE2Q8PqeHAgzIYvYC0lhraws5MZIfOXHCUVwYpO7ubhWXjFYGSyKQCvxUapGeGhobZbEeAinAiHwW6amzs1Pjxo1TBksikArIiROK4sIgNTY0BCu0ZApIBbbFtlBIO11dXRo3bpw8PrafRGoIsDQCaai+rk6yyDOQImyLQJxAFBcGwbIsFRUVKZMKLVIJW/AgzdTW1iojI5PtJ5EymGSDdGNZlgoKCtiSHaklQE6cKBQXBqGxoUEe2VRokVpYC4k0YoxRVlaWfBlZTg8FGJKATU6L9FFXt0PZ2VnBdexAqmBbyoShuLAXxhhlZGRQoUVqYgsepIna2h0qKSmRxeGMFMMxi3RhjJHX41GmONmGFBRgeXsiUFzYi7q6HcrNy5UsKrRIQVRqkSY6Ojpk85GFFGXTewFpoLGxUcXFJfIwMxKpiG0pE4JMbS+am5vlobCAVGXsYCMbIIW1traqrKxMYvtJpKgAJ3qRBjra2yksIHWREycExYUB7Ny5UxPLJrLVDlIbTWyQ4urq6mUbQyNHpCyz+w+Qqtra2jSutFQ+tmRHKiMnjjuKCwPYXLVJPq+HRo5IbVZApLVIVX6/XyWjS+SlkSNSnEVjR6SwHTtqZVizjlRHThx3FBf60dXVpZycXGXQyBHpgMaOSFHbt2/XiBEj2NIPKY/GjkhVgUBAOSNHKcvLQYw0QE4cVxQX+rFl82ZNnTpVXvotIB3Q2BEpyBgjj9crjzfD6aEAMUGRDKlo8+bNKh49mubmSA8B+obEE8WFfuzcuVO25RdTZ5AWjGF5D1JOXV2dSseNY5cIpA2LXSOQYowxat65k5MUSB/GJieOIzK2CJqamjRl6hRlsSQC6YRpYEgxO+rqFLBIAJA+mLmAVLN9+zZNmz5dGSIWI42QE8cNxYUItmyuUnFRMdO/kF6YBoYU0tbWpuLiYho5Iu0wewGpZNOmTcrJyWELP6QXtlSNG4oLe7BtW4FAQLI56JBuDMkBUsaGDRs1dswYzvQi7TAZB6miu7tbI7Kz5WVLdqQbQ04cLxQX9rB92zZV7LefMjjgkI6YBoYUYFmWWlpbZFFZQBriqEaq2LJls/bbf3/5bGbyIg2RE8cFxYU9bNtWowyvj0YfSE9MA0MK2FpTo4qKCnl8mU4PBYgLlkYgFWzbtk0+r5ecGOmJnDguKC700NXVpfz8AmXQyBHpzAqQ1SKpVVVVqbCwkCURSFssjUCya29v0+iSEho5Ir0xKyfmKC70sLmqStOmTZOXShbSGdtJIYn5/X75vD4KC0hrRiyPQHLbVLlJ+8yYIS9fvpDOWBoRcxQXemhqapId8IuPfKQ1EgUkserqas2cOVPyZDg9FCCuLJucFsmrsbFBhpmOSHfsDBhzFBd2a25u0pQpk5XlJYjCBQJ+EgYkpaqqzcrJGUWJF2nP4iBHktq5c6cmT56sLI/TIwESwCInjiWKC7ttrqpScXEJFSy4g8XSCCSfzs6u3YUFPprgDuSzSEabKis1oWwiDe/gDiwXjikyOEm2bSsQCEg2QRQuYVti+Q+SzZYtm7X/zJkyHp/TQwESgl0jkGyMMWpvb5fhCxfcgpw4piguSNq+bZv2mTFDGWy1AzdhaQSSTHV1tbIys/iIh2uwNALJpra2VuXl5cokEsNNyIljhuKCpMrKjRo5ctTuyhXgEpyVQBJpb29XUVGx5GXWAtyFnVGQTDZXVamoqIjmz3AXcuKYcX1xoaurS8YYeVhXBrcxtCpH8qis3KT99qug3wJch6URSBaBQECSodcC3IecOGZcn8VVbdqk8vIKZTD9C27E/r5IErU7auXxeInEcB1mLiBZ1Gzdqv33n6kMsUwYLkROHBOuLy6sXfuxSkpKmP4Fd+LsBJJAS0uLxo0rlceX4fRQAEcwewHJYMvmzRoxIptlwnAndlKLCVcXF3a1tmrkyBGyA3zBgksZO/gHcFBl5SbtO2Mf2e7+SIKLMXsBTuvq7JTH65WXnABuZQw5cQy4OpOrrq5WecV+yvTwqQ4XYxoYHGSMUX1DA1+u4Goc/3Ba1eYqlZfvKx9fruBm5MRRc3VxYf36TzRx4iTJYkkEXIylEXDQzp07NWnSRHkzMp0eCuAoCgxw0qfrPgnu2MMyYbgZ3wmj5triQnCXCO1eEsEnOlzMsNgXztmwYaOmTpki23icHgrgKJtQDIfsam1VRoaPZcKAscX3wui4trhQU1OjfffdVxnks0Bw9gJZLRLMGKOamho+xgEFmzoCTqjcVKl9y8tZJgxIUiBAThwF1xYXNny2XtOn7yMv078ApoHBEXV1dRo7dqw8Hp/TQwGSAuksnPDpJ59o8pQpLIkAJMlmVns0XFlcsCxLzc3N8no8dAUFJBIKOGL9Z5+pvHxfyUtxAZBYGoHE6+rslG3bMrbNwQdIu0+4MbV9uFxZXKitrdWUKVPlE4UFIIx9rZFAtm1r/fr1KiwspJEdsJtFWoIEq9m2TdOnT1cGZ2qBz5ETD5sriwubNm5QRUW5vIYDBwij7wISqKGhQWPGjFXAIg4DIURgJNrGzz7TvvuSEwO9kBMPm+uKC8YYVW/dqpEjR1GVAnpiS0okUHX1Vu07Y4a8viynhwIkFWbyIFFs29a2bTUalUNODPRCL7Jhc11xobGxUaWlpRw0wJ7YkhIJ9Mmnn2jKlCl8kQL2YBGKkSD19XWaUFYmEyAnBnox9CAZLtcVFzZXVWm//fZXBv0WgL6YBoYE6OzslBWw5PF4mAYO7IGCGxJl8+bNqqioYAtKIBJy4mFxXXFh48YNKikpoTs+EAlLI5AA27Zt09SpU2U8rvsIAgaFdBaJ8Nn69SotHc9nPxAJ74thcVVmt6u1VXl5ubIDHCxARKy5RAJs3Fip8opyediCEojIYkYu4mzXrl0aOXKELHJiIDJy4mFxVXGhurpaFRX7M/0LGAizehBHtm2rqqpKxUVFTP8G+sF7A/FWs3WrZszYVxmu+iYADBE58ZC5KqR8+uk6lU2cSDNHYCAB1pghfhobd2rs2LEKBDgjAPSHCIx4W//pp9pnnxnykhMD/SMnHjLXFBe6urrU2dkl2wqIj21gAFRpEUfV1dXaZ8Y+8mRkOj0UIKmxawTiJRAIqKW1WT6fL9gVH0Bk5MRD5priQk1NjSZOnCQfhQVgYGxJiTj69NNPNW3aNBnjcXooQFJjaQTipbZ2uyZPniqvYQYZMCBjKMANkWuKC5+t/1QzZuwjHwcIsHdWNwUGxFxnZ5e6urvl9Xop8wJ7QXEB8VJVWamKigpyYmAw2JJySFxRXLAsS5UbN6pk9BimtwCDwfIhxMH27ds0bepUueSjB4gaBQbEmjFGGysrVVRcTE4MDAZ9SYbEFRnejh21KikZLcvPdjvAoNiWJKatI7YqN21Sefm+EltQAoNis0oNMdbU1KSiwkJZ/m6nhwKkBrakHBJXFBdqttZo8uTJymALSmDwOKOBGDLGqLKyUiUlJZyNBQaJ9wpirbp6iyZNnswWlMBQMHth0FwRWjZsWK99ZsygcQ0wFGy/gxhqbGzU6NFj5LeIw8BgEYERa59+sk5Tp06Tl7OxwODZAXLiQUr74kJ3d7fq6xpUUFjItBZgKHi/IIaqt27VPtOny+djC0pgKJi9gFjp6uxUXV29cnJz+YwHhoKZC4OW9sWFHTt2qKysjLVlwFDRRRoxtP7T9ZoyZYpstqAEhoS+C4iVmm3bNGHCBHJiYKjIiQct7YsLW6urNWXqFGWQzwJDx5kNxEBXV5caGhs1cuQIpnkDQ8TMBcRK1aZKTZkylZwYGA5y4kFJ++LChg2fadq06fRbAIaDvX0RA9u312r8+PHyB4jDwFARgRErGzdu1NSpU8mJgeGw6LswGGldXOjs7FTTzp3Kzcuj2gQMh22J1BbR2rRpkyZPmiSvL8PpoQApiSiMaO3atUtdnZ3kxMBwsYvaoKR1cWFHba3Gs7YMGD7bksT8SQyfMUaffvqppk6dIpPeHzlA3NB3AdGq27FDEybQgwwYNopyg5LWmd6WLZs1adIk1pYB0aCJDaLQ0tKqzq5O5eXlc/YVGCb6LiBaW7Zs1qTJk8mJgWiQE+9VWhcXNny2YXe/BQ4EYNhYY4Yo1NXVaXzpeAUCTCcEhoviAqJVuXGjpk2fRr8FIBrkxHuVtsWF9vY2tbQ0q7CoiDUyQDTsgFjxi+Gqrq7WpEmT5KHfAhAVojCGq729Ta2tu1SQX8DUbiAafKfcq7QtLtTtqNO4caWyAn6nhwKkNou+Cxi+yspKTZs2TfKk7ccNkBD0XcBw7dixQ+NKxylATgxEx6I4tzdpm+1t3bpVEydNlI9aPxAlMloMT3t7u5qam1VSUsy0biBKvIcwXNVbqjVhQhk5MRA1I+aRDSxtiwuVGzdq2rTp8ol+C0DUmAaGYairq9e4cWNlWcRhIFoUFzBclZUbNW3aNHJiIBYscuKBpGVxoaurSw0N9Ro9ZgzTV4BYoIENhqFmW43Gl46XYVkNADiio6NDjQ31GjN2DP0WgFggJx5QWhYX6urqNGbMaBnbElNXgBggIcEwVG7cpKlTp8pLM0cgJpi9gKGqq9uhwqLi4H/4QgREj5x4QGlZXNhWU6Ox40p58YFYYTtXDFF3d3ewidi4cXwhAmKEpo4Yqu3bt2v8+AlM5QZihZx4QGlZXNhUWamJkyYp08tUXCBmKNZhCOrr65U9IlvZ2VnMHwNihEIdhqqqcpOmTptKTgzEEjlxv9KuuOD3+7VtW41KS5m5AMSU5eeUGQZte22txpeWyh8gDgOxQgTGUFiWpe3bt6lsQhkzF4BYIifuV9oVFxrq6+X1epWXm0dxAYglephgCKo2VWnS5En0WwBijNkLGKzGhgZlZGVpxMiRTOUGYonvmP1Ku+JCbe12FRUVyqJCC8SWbUl0/ccg2LatrTU1mjxpkuRJu48ZwFH0XcBg1dXt0PhxpbL83U4PBUgvFBf6lXZZ3+bNmzWhbBIvOhAPnPnAILS0tMjv96uoqIizrECM8Z7CYAVz4jJlcF4AiD1y4ojSqrhgjNG2bTWaUDaBxjVAPLC3Lwahvr5BxcXFsjlWgJjjXYXBMMZo8+bNKisrk5ejBog9cuKI0qq40NHRro72do0bO46ZC0A82Cw3wt5trdmqCePH85kLAA7ZtWuXOtrbVVxcTE4MxAPvq4jSqrjQ2LhTHq9Xefn5vOBAPPC+wiBs3rxFU6ZMkdeX6fRQgLTE0gjsTX1dnbKyMpWdnc30bSAeyIkjSqviQkN9nQoLi2RbvNhAXHAqGnvh9/tVX1+v0tJxfAEC4oSmjtibmpqtGj16rAIBv9NDAdITRbuI0qq4sLW6WhMmlDF1G4gngikGUN/QIK/Xq5ycHFb5AnHCewt7s3lzlcaXTZCXz2wgfnh/9ZFWxYWa3c0cM2jmCMQP26/sU84AACAASURBVLxiAHU76pSfnyfL5gMXiBdmBWEglmWpvr5e40tLyYmBeGK2fB9pU1zo6OhQ265dKh1XKg9JLRA/tsV8XPRrS/UWjS8tlc23HwBwREtLi4xtVDJ6NOvCgXiy2TFiT2lTXNjZ2CiPx6uCggICKRBPvL/QD2OMqrdUq7S0VF5fhtPDAdIa9Tv0p2nnTklGeXk0OAfiimURfaRNcaGhoUH5+fkyxharEYE4IpCiH21tbWrv6NDYseMkT9p8vABJyYgTZoisvr5e+QWFsiksAPHFe6yPtMn+tm7dqvFlZbJZDw7EHwUGRNDc3CyPx6PCwgK+9ABxxswF9KemZqsmTJggQ04MxB8JTy9pU1zYVrNVZRMmKMND4xog7qjUIoLGnTvl9Xo0YsQI5o8BcUY+i0iMMaqt3a5xpaXkxEAisEthL2lRXOjq7FRzc7NKS8ez5Q6QCDR1RAS122s1buxY+QN80ALxRgRGJB0dHepo71DpuHHyipwYiDty4l7Soriwc+dOeb1eFRQWckYVSATeZ4hg+/ZalZaWyoizZUAikM5iT01NTZLHo8LCIond04D4s+n311NaFBcaGxuUk5uzO53lxQXijoQFe7AsSw0N9Ro7dqx87BQBJAR9F7CnnY2NysrMVEZmJv2RgESwLYmTKmFpUVyoqanR+PE0cwQSh4wWvbW2tso2RqNHj2HmApAgxjAbF71t375NpePHy/L7nR4K4BIE4Z7So7iwdavKyiYoIy1+GyBFsDQCPTQ1Ncsjj/Lz8zmbCiQI7zXsaVtNjUrHj5fXw8EBJAyzhMJS/uu439+txp2NKi0tpZkjkEgUF9BDY2OjsrKzlJHhc3oogGvw9RE9BZenNai0tFQZTCADEsciJw5J+eLCzp075fV4lJefzzpwIJHojosetm3fpgnjSxUI8AELAE5oamqSx+NRSUkJJwCARDLkxCEpX1xobGyUjDRixEimpACJZOiOi8/Vbq/VuHGlkjflP1aAlEI+i5Cmpp2SpNycXIoLQCLZlsiJg1I+C6zZulWFxSWyaOYIJBbdcbGb3+9Xc3Ozxo4dI6+XnSKARLJFgQFBdTvqVFxcLIsp2kBikROHpXxxYevWrRo3bqwMgRRwABktpObmZnm8XhWXlHBEAAlGYQEhNTVbVTphgmRzwg1IPIKxlOLFhUAgoMaGBhWXlMhHsQhIPPqcQNLOpiYZ2ygvN4/u9UCC8Z6DJBljtKO2VqWl4+XzkBQDCUdOLCnFiwutra3yeDwqKiqiuAA4gaaOkFRfX6/8/HwZqvZAwvGugyS1tbWpq6tLY0aXyCu+5AAJR04sKeWLCy0yMiosLKRaBDiBBjaQtK1mm8aPL5VlEYcBwAlNTU2SR8rNzSMnBpxAE1VJqV5caGmVsU0wkLJTBJB4xhYNbNzNGKPaHTs0btxYeb0+p4cDuBIny9DY0CBjG40cye5pgCPYRU1SihcX6uvrlD0iW1lZWQRSwAmcHXG9zs5OdXZ2auzYsfJQXAAcQSTG9u01KiwqlE2lCXAGJ9wkpXhxoa6uTqNHj5EV8Ds9FMClSGLcrqmpSR6PR4WFhTSWAxxiDLMX3G5bzTaNGTNWdoCdIgBHEIQlpXhxobGxQaNHj5ZhjQvgHGYNuVpTU7Ns29bIkSMpNQEO4b3nbpZlaWfTThUVFcvDPBbAORQYUre40N3drfa2dhUWFrHlDuAkiguuVltbq5xRo+QhDgOOIZ91t127WuWRR3n5ecrwEosBx5ATp25xobWlRV4v21ACjqPvgqtt27Zdo0eXKGAxgwxwCrUFd9u1a1dweVpBoTxUmgDnkBOncHFhV6tkpIKCArb+AJxkbE6buZRt26qvr1NxcQmHAAA4ZFfrLhljlJfP7mmAo4zl+pw4ZYsLzc3NsmWUk5tLIAWcZLP1jlu1tbUpYFnKz89jpwjAYURh99q5c6c8Ho9yRuWQEwNO4v2XusWF+ro6jRqVowyfz/UVIsBRbL3jWqGpuPn5+fJSXAAcRSrkXg0N9crJyZEvI4MDAXASyyJSu7gwZuxYBdiGEnAWVVrX2tXWJhmjvPx8zpoCDuM96F6NjY0qLilRwE9ODDiKnDg1iwvGGDU0NqikpEQeXkQgCZDWulFrS6uMpNycXE6WAQ4zhpPWbmSMUdPubSj5YgPAaSlZXOjs7FR3V7cKCwrZhhJIBmS0rtTQ0KDMjEyNHDmC8hLgMN6D7tTR0S7bspWfn8/uaUAycHmRLyWLC62tn29D6eXjFHAeO7a4UuPOncrLy3V6GABEjdetQr1vCgoKKC4AycDlfRdStLjQKhPahtLl1SEgKbAdpSs1NTWpuLhYAYviEuA0IrA7BXNio4KCfNd/qQGSgsu3o0zJ4kJzU7MkaVRODoEUSAZsR+k6gUBAbW1tKijId/NnKAA4qqW5RZJRTg5bswNJweXfTVOyuLBjxw7l5+cr2G6BrBZwHNtRuk5bW7u8Hq9yc/Pk9bENJZAMKPS5T2NjgzKzspU9YgTFBSAZuPx9mJLFhYb6OhUVF8sKBJweCgDp/7N33/FRlPkDxz8zO7ub3iD0TgpVOgEUFBSxUKzn2fvp6VlOUU8sp6h4pz/7eU3PdmcXFVGxgBWF0CGhhJBAIHRSt5eZ+f2xIRAJVbK7yX7frxdKdmZ3n80wzz7zne/zfWK+I41FTqcTFOoCvRJcECIaSE8ce/bs2UNGRga6LmNiIaJCjI+Jm11wwTRNKqsqSUlJifmDJ0TUkNtlMcflcmGaJikpKZI/JkSUkOUoY091VRXpGRmYUvtGiOgQ451wswsuuFwuDN0gMTGp+TVeiJYsxjvTWFNbWwOmSWJiohx6IaKEnIqxxe/34/V6SEtNk9XThIgmMTwwanbX506HA0VRiE+Ix6LKHG8hooZkEsWUispKbDYbcXFxMqQVIkrE8Hg2JoWWoVRJSUmRMbEQ0SSGx8TNLrjgcNRimibJSUlSPk6IaBLj1XFjTWVFFampqZgx/AUqRLSR2EJscTodAKSmpaJIZEmI6BHDY+JmF1yorXVgAomJiTEdFRIi6sT4ur6xprqmmrS0NHRd+mEhhIgEp9OJYRgkJyXLmFiIaBLDY+JmF1yoqanGatWIj0+I2YMmRFSSgU3MCAQCeD2eUOaC5JAJEVVkZBQ7KisqsGiaLEMpRLSJ4fOx2QUXamtq0TQr9jh7TB84IaJODKeAxRqXy4WiqiQlJaFaZBlKIaKJ3HeJHRUVFdjtdqyaJgdeiGgSw2PiZhdccDhqsdlsWK1W6UiFiCZyPsYMl8sFQGpqKorS7L5GhGjRpCeOHZWVlSQnJ2PE8IWMENEpdnviZjcqdDqdJCUnowdlPV8hokvsdqSxxuF0YhomySnJctSFECICdF2ntqaG5ORkdF3GxEJElRi+4dasgguBQACfz0dSUhKGIR2pEEJEQm1NDYoCCfEJsfz9KURUMs2YHtfGDLfbDQrEJyTINGEhRNRoVsEFr9eLoqgkJCTE9FwWIaKWjGhjQkVlJVabDZvNKpkLQkQZOSdjg9vtRlEU4uPiUOSoCxF9YnRM3KyCCx6PG0WB+Ph4VClQLkT0kbsnMaGqsgq7zY6maZFuihBCxCSvxwMmxMXFoyoyKBYi+khwIep53B4AEuLjUSW6IET0idEobayprqkhOTkJXZdgkhDRRrrh2OD1ejFNk/j4eCwSXBAi+sToDbfmFVzweDBMg6SkZFT59hQi+sRoRxpL/H4/Xq+XhIQEqVAuRBSS0VFscHvcACQmSs0FIaKSEZu9cbMKLjgcDhRFqetIY/OACRHVpJJYi+dyubCoFuLi4jDkWAshREQ4ah1YNAvx8TImFiI6GTF5bjar4EJNTQ1WzVrXkUqUVoioI+dli+f1ejExsdvtkW6KEELELIejFs2iERcXh+SrCBGFYjCwAM0suOBw1KBZrdjj7DF7wISIbnJetnQ+nw+AuDg7itKsvkKEiBnSE7d8TqczNCa22yWwL0Q0itHzslmNDB21Duw2GxaLhnx1ChGFTBM5N1s2r8+HaZrY7XGoFkukmyOEaIx0wy2ey+lE0yxoVqvccBMiGsXoedlsggumaeJ0OklKScHQ9Ug3RwjRGNMEpGp1S+Zxh5Y/S0iIR461ENEpNoe0scM0TVxuNwkJSZhSWFeI6CTBhegWDAYIBPwkJiZKcEGIaBWjKWCxxOVyYbGoxMcnyAWMEFFKzs2WLRAIoAeDdav2yJhYiKgUo2PiZhNc8Lg9KIpKQkICEJsHSwghIs3hdGDRNOLi4yLdFCHEQcjCPS2b1+tFVVXi4uMkc0EIEVWaTXDB7fGgoJAQH998Gi1ETJIRbUvmcrnRLBbsdrtcvAghRAR4vR4A4uPiUOQ7V4goFnvnZ7O5Tvd4PJiYxMcnYFFlnq8QUUuuOFs0t8uFpmnYbbYY/MoUonmQc7Nl83q9AMTFxaEqMiYWImrF4Ji4GQUX3BimQXx8vJQQEyKaxWBHGktcbjeapqFpWqSbIoQ4COmGWzavx4tpmsTFxyP324SIYjHYGTeb4ILT4UBV1Lr1fGPvQAnRbMRoAZtYYBgGXq+XuLg4TOmHhYhacna2bB6PG9M0SUxIRJG+WIjoFYNj4mYTXKiprkGzWrHbbRJcECKaxWBHGiv8fj+YoVRcXYqICSFERDgcocK6oSLnMiYWImrF4DVr8wku1NZgtWrYbHakIxUiikmZ8hbL5/OhqEooc8GQYyyEEJHgcDjQNI24uDj5vhUimplGzJ2jzSa4EOpIrVit1pg7SEI0K6aJBABbJp/PBxBaKSLCbRFCiFjlrAsuhKYKSxaZEFErBsfEzSa44PHUFRGzahJcECKayfnZYu2tUG6320EqlAsR1aQnbrmcdav2WG0yVViIqBaD5+dhy33n5uZy8803M2/ePLxeL3fccQcTJkwA4M4772Tjxo0EAgG6dOnCjBkzSE1NpbS0lHvvvRePx4NhGJx77rlce+21zJ07l+eeew5VVdF1nQceeIC8vLzDNtIwDPw+P2qqisWiQSD2DpQQzYZpgKzp0iL5fD4wTeLi7KiqBblfJkT0Mk2kK26h3C4XGa1aRboZQojDicEx8RGtJaaqKrNmzaK0tJSLL76YoUOH0qpVK+677z4yMjIAeOaZZ3jppZeYOnUqb731FuPGjeOGG24AoKamBoDnn3+e6dOnM2jQIHRdx+PxHFEjA4EAiqKElj6LwQiQEM2LnKMtldfrwzDN0JLAiiqHWogoJqdnyxQIBAgEAtjsdgxdbz4pyELEpNjriY8ouHDhhRcC0KNHD/r06cOKFSs49dRTmTVrFrNnzyYQCOB2u+nWrRsAw4YN48knn8Tj8ZCXl8eIESMAGDFiBI8//jinn346Y8aMIScn54ga6ff7URQFm82OYRjSkQoRzSQA2GI5XU4sqlpXoVwIIUS4eb1eFFXBZrViSr0FIaJbDI6Jj/k6fcmSJbz99tu8/PLLzJ49m9tvvz20TBkwYcIE3nzzTbp06cJLL73EXXfdBcC0adN45JFHsFqt3Hbbbbz33ntH9F6h11Ww2awYhn6sTRZCCPEruJwuLBaNuLj4GIzFCyFE5Hm9XhQUrFYrZgxeuAghotsRBRdmzpwJwKZNm1izZg0DBw6ktraWpKQk0tLS8Pv99fsAlJWVkZmZyXnnncfNN99MQUEBAKWlpeTm5nLllVcyefLk+scPJ+D3AyY2KVwjhBAR43Q60TRLaLUI6YqFiGqyKnDL5K2bUiyrpwkhotERTYvQdZ1zzjkHj8fD9OnTadWqFaNHj+aTTz5hwoQJpKenM3To0PpgwZw5c5g9ezZWqxVFUZg2bRoATz31FGVlZVgsFlJSUnjssceOqJH+QCgjwmazEYtzV4QQIhq43HUVyq3WSDdFCCFiks/nw8REs1qRMbEQItocUXDhmmuu4ZZbbmnwmNVq5dlnn210/xtvvJEbb7zxgMdffPHFY2gi+H3++veMrXqbQjRXUqa8JXK7PGiaBYtFlSGtEEJEQCAQAFPGxEI0H7E1Jm4WtRH9AT+GYaBJRypE8yBXni2OaZq43W40TcNisUS6OUKIw5BuuGUKBAKYpolVkzGxEM1CjHXGh81cKCoqCkc7Dsnn9YICVs2KqkhXKkT0i7GeNAYEg8HQaj2qimqxgNTWFULEmNzcXG6++WbmzZuH1+vljjvuYMKECQDceeedbNy4kUAgQJcuXZgxYwapqamUlpZy77334vF4MAyDc889l2uvvZa5c+fy3HPPoaoquq7zwAMPkJeXd9g2eH0eVFXFapUxsRDNQ2yNiY9oWkSkeTweLKoFzapJRypEcyBFplocr9eLooCqqnXHV/piIUTsUVWVWbNmUVpaysUXX8zQoUNp1aoV9913HxkZGQA888wzvPTSS0ydOpW33nqLcePGccMNNwBQU1MDwPPPP8/06dMZNGgQuq7jqSvUeDhejxfVIsEFIUR0ahbBBbfbg0WzYLfZibXojxBCRAO/3w+KgqZpsvyZEM2AnKZN48ILLwSgR48e9OnThxUrVnDqqacya9YsZs+eTSAQwO12061bNwCGDRvGk08+icfjIS8vjxEjRgAwYsQIHn/8cU4//XTGjBlDTk7OEb2/z+tDVUOr9siYWIhmIMY642ZRc8HrcaOqFlmKUojmQs7TFicYDKIooGkahmFEujlCCBE1lixZwttvv83LL7/M7Nmzuf3220MBWWDChAm8+eabdOnShZdeeom77roLgGnTpvHII49gtVq57bbbeO+9947ovbxeLxZVxWaTpSiFaB5i6zxtFsEFn9+PpS4FTAjRHMRWRxoLgkEdTOoyFyLdGiGEiIyZM2cCsGnTJtasWcPAgQOpra0lKSmJtLQ0/H5//T4AZWVlZGZmct5553HzzTfXL9teWlpKbm4uV155JZMnT65//HB8fh+qxYLVKsuzC9EsxNigqVlMi/D5QilgVonSCtE8yHl6XEVDEbFgMIhZH1yQ4ytEtJOztGnous4555yDx+Nh+vTptGrVitGjR/PJJ58wYcIE0tPTGTp0aH2wYM6cOcyePTu0dKSiMG3aNACeeuopysrKsFgspKSk8Nhjjx3R+4emRahomiYHWYjmIMbO02YRXPD7/aHKuJqVcB2hktKNPPyXJ1i9dh0Z6encffstjB83FgCPx8tfn3mOOV/PJRgM0is7mzdf+Xejr1NdU8N9Dz/KTwvySU9L445bb2LSmWfUb5895wuefv7vVFVXM2rEcGY89ABpqakAPPbk03w8+zN6dOvKc08+Tru2beufs3JVIfffM7WJfwtCHKsY60nDINJFxILBAChmKLjQNB9RCCGi3jXXXMMtt9zS4DGr1cqzzz7b6P433ngjN9544wGPv/jii8f0/n6/D4ulLrggvbEQzUBsnafNYlqE318XpbVqYbkjGgwGuemPUxk7+iQWfTeX6fffy133/ZmNZWUAPPDoDGpqapkz8z0WfTeXe6f+8aCvNf3xJ7Farfw07wuenDGdh2b8leKSEgCKS0p48NG/8MSjD/HTvC+Ij4vj4RlPALCqcDWr167lp7lzGDxoIP9+9Q0AHA4n/3n9f9x+84FfVEJEDRPJXjjOGisiBjBr1izOO+88Jk2axKeffsratWuBUBGx999/n2effZYFCxaQkpIC7Csi9vLLL1NSUkJSUtIRvX8wqNdnLgghhIiMvdm8Fosl0k0RQhwRM6bGxM0kuODflwIWBqWbyti1ew9XXXYJFouFkcOHMXjgAGZ9OoeSjZv45vsfeeSBe8nISMdisdCvT+9GX8ft8fDVvG+47aYbSExIYOiggYw7eQyzPp0DwOzPv2TcmJMYNmQwiQkJ3HbTjXz9zbc4XS7Kt25jyMCB2Gw2Rg4fxpbyrQA88+I/uPbKy474gkCIyIidTjSSwllELDQtwpTgghAiZhUVFZGYmBix9zdNs35MbNEsMXXBIkSzFWPnadQHFwzDIBgIhjpSS3gyFxpjmibFJSUUFK6mY/t2PP/Pf5M3djyTLryYL+d+0+hzNpVtxqJZ6N61a/1jvXKy2VBaCkBxSSm5Odn127p07oTVamVT2WayevZgyfIVeL1eFixaTFbPHhSsXsPGTWUNplUIEZVirCMNh0gXEQsEAkBd5oKsrS6EEGFnGAaGYYTGxKoFCeQLIaJN1AcXgsEgAIqiYFFVwtGRdu/alYyMdF5+/b8EAkHmL1jI4qXL8Hq97Ni1i/UbSkhOSuLHrz7ngXvu4k8PPkxJ6cYDXsftdpP0iwh3clISLpc7tN3jJvkXGQhJSUm43G5ysnoy4dSx/OaKa9i+YwfXX3k5jz3xFPfffSdvvPUul17zO+6c9gC1DkfT/SKE+FVk0HM87S0idsMNNzQoItalSxcmTJjAZZddRp8+fer3nzNnDpMmTeKcc87h0UcfbVBEbOLEiUyZMoWff/6Z66+//ojeP5SKq2KxqChIcEEIIcIttCRwqP9VLZawfc2WlG7kit/9niGjxzJ+8nl8/c239ds8Hi8PzfgreWPHM2T0WC695ncHfZ3ybdu4/g+3M2zMqZx42hlM/8uT9eN8gLVF6znvkisYMHI0511yBWuL1tdvmz3nC04afybjzprCwsVL6h/fvKWc3155LbquH+dPLcRxEmM33KI+vzUYDNR3pEqY7pZZrRovPv0kj/71/3j5tTfo16c3Z5x+GjarlTi7Haum8fvrrkHTNIYPHUzesCHMX5hPzx7dG7xOQkICTperwWNOp4vExITQ9vhGtrtcJCaEtl912SVcddklALz57vsMHTwIwzR478OP+Ojt//HSa6/z71deZ+ptf2iqX4UQx8gEuQA9riJdRMzn86EqKqpqkcwFIZoJ6YlbFl3fF1ywWFQIhq8O2W8vOI9X//E3Fi1dxu9vu5OP3ulB965deeDRGehBnTkz3yM1NaVBQOCXHp7xBK0y0pn/9efUOhxc8/tbeOu9mVxxyUX4AwFuun0qV176Wy75zQW888FH3HT7VL78ZCaqovDU8y/y4Vv/ZfXatTz61//j0w/eAeDRJ57i3ql/lBoUIorFVnAh6jMXAoF9wYVwDmh75WTzv//8i/zv5vKfv79AeflWTujXl9zsrEb2brxd3bp2QQ/qbCrbXP/YuvXryerRA4Dsnj1Yt764ftuW8q0E/H66de3S4HX2VFTw7syPuPl311G8oZTc7CysVo3+fftQVLzh139YIY43s/4/ooXw+fdmLljCFugVQgixTzC47+68qobnYvp41SGDUObCmeNPw263k9m6NSeNGlk/VXjRkqUEdZ0rL70Ym83GFZdchInJwkVLqK6poW1mJm0yWzMqbzhbtobqkH3x9TzatslkQP9+YfldCHFMYmxMHPXBhWBgX7pUOAe069YX4/P58Hi8/OeN/7Frzx7OmzyRoYMH0759O/71yusEg0GWrlhJ/pKlnDRyxAGvkRAfz/hxY3n+H//G7fGwdMVK5n3/A1MmngnApLMm8O0P81mybDluj4fn/vEvxo8be8BUisefepZbbrye+Pg4OnXsQMHqtbjcbhYtWUbnTh3D8vsQ4ujETicaDpEuIgZ1hXUtddMiwtQXl5aUcN3VV3Bi3hAmnjGeeXO/BuCzTz9hxNBB9X/yhgxgQN9c1qwuPOTrlZVtYtig/tz7i2V8P/90NmecNpa8oQO5/ZabqKmurt/2xOOPcdLIYVx+yUXs3LGjwXP+MuPR4/hphWgC0hW3KHrdFAJVVTEjmGp9LHXIAK685Ld89uVXeDxedu7axY8//czoUaHx84aS0M2z/b9fcrOz2FBSSkZ6OtU1NezYuZOfFi4iq0cPnC4X/3j5Fe645aYm/7xC/DqxlUMW9cGFvUXEILzBhVmfzeGk8Wcx6tQJLMhfzKv/+Bs2mw2rVePvzzzJD/N/YujocTwwfQZPPPJnenbvBsA///Mq1918W/3r/Hna3Xh9XkaNm8Cd997PQ9PuIbtnTwCye/bk4fvuYep9DzJq3ARcLjd/nnZ3g3YsWLQYh8PJ+HFjATihX19OHn0ip5wxifwlS/nd1VeE5fchxFExY6sjjQV+XwBVUepWi2j6YxsMBrntlpsYc/JYfvh5EQ88NJ1pf7qLTZs2cvbEySxcsrz+z7T7/0ynzp3p3afvIV9zxqPT6duvf4PHNmwo5pGHH+SxvzzBt9//RFxcPI89+jAABatWsWbNar75/icGDR7Mf17+NwAOh4PXXv0Pf7j19qb58EIcJxJbaFmCdXUFLBZL2IILx6sOGcCwwYPYULqRIaPHMmbCRPr16c1pY08BwOX2HKQOmQtVVXlo2j3cete9vPLG/3j0wft44R//5rLf/oai4g1cfv3vufamW1i/oaSpfx1CHD2puRBd9nakiqJgmmbYLlfu+eOt3PPHWxvdlt2zJ+++8Uqj22689mq4dt/Paamp/P2Z/zvo+0w684xDrv4wcvgwRg4f1uCx++66g/vuuuMQrRdCiOMrqAf2rdoTBhs3lrJ71y4uv/IqFEUhb8RIBg4azKefzDrgov6TWR8xafI5hwxAz/n8M1KSk+kxcBCbN5fVP/75p7M5+ZRxDBka6mdvvuU2zpl0Fi6Xk61byxk0eAg2m428vJG89eZ/AXjhuWe46uprZUlgIURY7c1c0DQN0zDC8p7Hqw6ZYRhcd/Nt/Ob8c3jntZdxud1Me+hRnnzuBe6+/VYSE+IPqEPmcrlITAhl7Y3MG87IvOEArCtaT+Gatdz9x1sZd/YU3nrlJbbv3Mn90x/jvYOMz4UQ4RH1mQt7O8+9wQUhRDMg52qLEwyEColpWgSLZpkmGzYUN3ho27atLFu6hImTpxz0aU6nk7//7Xmm3n3vAdtKNhSTk5tb/3PnLl2wWq2UbdpEz6wsli1dgtfrJT9/AT2zslhdWEDZpo2cNXHS8ftcQjQR6YlblkhkLsDxqUNWXVPLxzWc0wAAIABJREFUth07uOyi32Cz2UhPS+P8KRP5Yf7PAGT17EFR8YYGn6to/QayevZo8DqmaTL9r09y/z1TqaquRtcNOnZozwl9+1BU3PD7QYjoEFs9cfQHF+o6GUVR5IJFiGZDztWWJrQEWvgyF7p1605Gqwxee+VlAoEAP/80nyWLF+P1eBvsN3vWxwweMpROnTof9LVefOFZzj3vfNq2a3fANrfbTVJycoPHkpKTcLlcZGfncNr4CVx+8W/Yvn07V11zPX99/DHuufd+3vzfG1x9xaXce/ed1NbWHp8PLYQQh6DXL88enqXZ9zoedcgy0tPo1LEDb78/k2AwSK3DwUezP6sPUAwfOgSLqvLG2+/i9/v53zvvATBi+NAGr/P+R7Po06sXvXNzSEtNxefzsaGklIWLl9K5o9QhE1Eoxq5foz64YJgGYIaK10S6MUIIEaOCuo6qKqE7ZmF4P6vVyrPPv8iPP3zPqSefxBuvvcrpZ5xB23ZtG+z36SezmDTlnIO+zrq1a1m4YAGXX3FVo9sTEhJwOZ0NHnM5nfUFNC+/8ire/+gTnnzqWb76Yg6DhwzFMA1mvv8e//7Pa3Tv0ZNX6moxCCFEUwrqwVBpuDCXNDpedcj+9tQT/PjzAkaOm8D4yeehaRr3Tv0jADarlRefeZJZn37O0DGnMnPWbF585klsVmv98yurqnnjrXe4/aYbgND0kAf+dBdX3nATDz32F+7/RbFeIUT4RX3NBdMIFYaTzAUhhIgcPRjEYrGEdVpETm4vXnn9f/U/X3HpbxsEEpYvW8qu3bsYf/qEg77GksX5bNu2lQmnhYriut1uDEPnopJzefeDj+iZlc36onX1+5dv2YLfH6Brt24NXqdizx5mvv8ub7z1Lt9/9y05OblYrVb69uvPW/974zh9YiGEODg9qBOJzMDjVYesd24O/335nwd9nz69cvnwrYP3pxnpaXz6wTsNHpt81hlMPuvgtcuEEOEV/cEF06yL0iqYkrsgRPMR7lsrokkFgzqapmGxhC+4sL5oHV27dccwDN575y12797FlHPOq98+e9bHnDb+dBITD15Y8fwLL+KMM8+u//n1115h29at3PfgQwCcNXESV1xyEcuWLqFX7z68+LfnOHX8+ANe8/+eeJwbb76F+Ph4OnbsxOrCAtwuF0sWL6LjIaZkCCHE8aLr+r6aBDIkFkJEoWYRXFAIrekrHakQQkRGUA+iqvGoYQwufDp7Fh/O/IBgIMjgIUP410uvYrPZAPD5fHz15RyeevaFA5738r//ybKlS/j7v14mPj6e+Pj4+m0JCQnY7DYyMjIAyMrK5v4HH+beu6dSXVPNiBEjmf7o4w1eL3/hAhwOB6eeNh6A/iecwOgxJ3P6aafQrVt3nnrm+ab6FQghRD1dD9aNhSV4L4SITooZ5UswFBev5/NPP6Vrt25MnDgRLeCJdJOEEEciPkWyF1qQZ597nlYZGZx11lkkp2VgRPU3hxACwKKApkpX3FKsWL6c7779hqzsHE4//XRsuvfwTxJCRF5CaqRbEDZRX9DRNPatFhHdYRAhhGiZTNPE0A2ZniaEEBFkYoIiwSIhRPSK+uCCYRpg1k2LkEGtEEKEnWEYdQNaKawrhBARI/2vEM1TDJ27UR9cMA1z36BWCCFE2Om6Xv/32Pl6FEKIaCa9sRAi+kR/cAETTLNuWoR0pEIIEW66rtcHeKUfFkKIyDD3FnOUG25CiCgV/cEFo24pSjXqmyqEEC1SaNUeZe8PkW2MEELEOAktCCGiVdRfsZumgQmoEqUVQoiI2VvIUUILQgghhBCiMVEfXNANA9hbSCzCjRFCiBjUoOaNZC4IIUREhLLIhBAiemmRbsDhGLqOouydFiGD2pYoqNowZdpLi2CaoKoKmhb1XYs4CvsHF6TmQsukABb00MogotkzTROr1SrFsFuY+qWA5bi2WEGLDVORMXFLEKtj4qj/tIYRmusr0yJaLg2dACr+QJBly5ZSVVkZ6SaJY+RwOOncuRNjTj4l0k0Rx9V+wYUItkI0HRMwFQsmBjarxs6dOykpKaWiokICSs1QZVUV5593LikpKZFuihDiKGimTgCwWO1s2bKZoqIivB5PpJsljkGtw0HXrl0ZPXpMpJsSVs0guGCgKIpE31syQ8dq6Fg0KyNHjqR8SznLli3D65XOtLmpra3B5UqPdDNEU5ILzRZLNwHVil+HjNZtyGjVimAgwIYNJWzcWIrT6Yp0E8URqqmpabCErGghzLrl2SPdDtF0DB0rOhhBOrZrS6eOndiyZTOrV6+mpqYm0q0TR8FRU4PbFXvfm80iuICioEiKUIun6gFUPUDnDm3p1Gkya9asYe3aNTJAakYUkFvbLZCiUH9cJbbQ8pmAiQqKisVmpVfvPvTp05vaWgfFxevZvHkzfn8g0s0Uh2JKV9wS7et/JbzQ4pkGmu4HPUCXDu3o1LkzlRUVFBQUsnPnjki3ThwJRYnJzL/oDy7oOgqhOSvyVRkbLHoAjCB9euWQk5vD0iVLKSvbFOlmiSOhKPvmhIoWQ9nvuMbiF2Us2ztdwgCSUtMZOGgwQ4cOZceOnWzYUMy2bduPqE5D1+7dyWzTpsnbK0K8Pj9Wexy+YNPW0FAVsFrk5o8QTcesv/mWmZbCmDGj8Xp9FBQWsLmsTOrkRDnTiL0xU9QHF/S6zAXDMJFIbQwxTTTdj6ZaGDZsKLm5uXwzby47dki0NpoFAn6ZwtQCNTymsfdFKUKMumkTARPatOtAq1atUFWF9euLKSwsZMfOnQd9blpGOlk5ubRrnUGtN8iS8lp2OHzha3zMSWB1UXWTv8v5/ds2+XuIfUxCdchkOBybFD2AlQBWm8bQwYMZPGgwS5cuoaCgAL/v8P1pYmIio0eMQL7Hw8M0DFJSUzHDMc3bZq9b/CDyoj64YBih1SJ0Q1LjY5KhY0OnVUoCF1z4GzxeDxUVlUc8VUJVVeLi4pq4kWJ/UkCsZVLqRrOSuCCgrj6DZscEcnv3oXfv3pimgcPhwOl0EgwGD3iOx1FDuddNQmISo7qkUO0NMn9TNUvKa3H45Du+OTqnr2SjhFeoA5bYQowzgtgAFJWRecMZOepEnE4nNTU1jfa9e1ksFjJTkohLTYfKXRg/zoHaqrA1O1Y1dW6J0nsQysBRoNqa+J2OTDMILoSitIauI91p7FL0IIruJNFmJ7Fz57oHD//vYV8KtwnVu8GU9LEm56nG9DTxHbO4JIhPkiyJMFH2K7og0yLE/kxANxX00LpOJKemk5YWKup6uNOznU1jcp82TOnbhrIqLz+UVrFqu4NADKaRNlvSBQsROaaBGvBC0EdKvJ2U5E6hx49kfJyShnr2JZjLf8L44l3YsaWJGyuaTEISyqATI92KelEfXDDrpkWEpkdEujUi4gI+CPrBGgcWa+ixQ3Siey8+zWAQElIwihbBrrJwtFQ0IaX7CSg9BkS6GTHFbORvQuzPBIIGBAnNxbcoof/DwbtpmxZK48xqnUDHVDuXDW7Pqu0O5m+qZsMet/xri3IyLIsU+c2L/ZgmBLyhP5oNrHZCy4ocYnxstYf+MmQ0loGjMDetx/z8Lcz1q8LTZnH8RNmNtqgPLuiGgUJdYcco++WJCDFN8HtA9YMtHlAPe2IpmhU0K2qfUdCtH8baheCoCE97hWjm9u97JXFBHAnDrKvRQCjIgKmjKgo1DgfVNTV4vI3PD9YsFjqmJHPNkLagWMjfXMOCLTXsdPjD13hxxGRUFmbmQf4uxF5Bf+iPxRoKMuxdbe8g42TFooFFg+x+KDc+CLWVGJ+9hbn0R5Ap6c2DohBNvXHUBxdUVQmlXcq0CPFLhg5eZ6gDtcVxuCgthIIMZnIG6tAJmHvKMdcvBl8YCq2I40tRJNgYbvVLUZrSE4ujopsAFgwTEhOTSIiPx+fzkb9sJUtXFVJVU9vo89q1yWTwCf24dURfan06+eUulpTX4vTLgDdqSD8cVnuDu/JrF4elB0J/VAumZsNULFRX7KF6z270Q9RlSEhOodWUq7FdcD3m3A8xf5wDXncYGy6OmqJG1SVy1AcXNM2CaZoYhiEXE6JxegA8AdDsdalgEAgECAQOvQ67Na0d2shzMTavhk2FEqEV4iAUZV91cllqVBwrE0CxgMVCXIKNk0eNYOxJI6iqrmHVmnUUl5bh8zfMUFhRsJqVhWvo3KEdfXJymDi+O6V7XCwsd1Kw3Sn1GSJMRmURIGNhcTQMHcXvQVFUkpMSSUlLZ0PhKhZ98zWVOw++Altmx07kjT6Zbo9ciLlwHsq3H0Pl7jA2XBwxVTIXjoqmWTENA12mRYjDCdbVY7DFoSgKC77/hlVLFqMeYmmW5NQ0Thk/ns4jpmApXYG5ozSMDRbHTvqCcGrQ98q8CHEcmACqhg6kpbfipLzhnDIqj83btlOwpoiyLVsxzH1FRDdv3c7mrduxaho9u3dhXE4OFw/oycptteSXO6U+g4gJewvq6rouX4Pi6JgGVoCgl+w+vcnqdwIVu3ZQkL+AnVs2N/qU/B+/p2D5MnoPGEjWtBcx1i5HnfsBlBWHteniMJTDTw8Pp+gPLlg1TNMMBReiZP1OEc1C9Rg0ReWU8aczbNRJfDvnMxyO2oMGGRbO/5ENbYvJGzmKhE65qMVLoEais1EtijrRmFE/LSKyzRAtj2ECFitBoHPHznRo2xZFUSgqKWX1umJ27t5Tv28gGGRdcSnriktJTIgnN6sHF/fNwWZvy6ItteRvcbDTGZ76DEYwwLqP/0nlhlUE3A7iW7Uj64zLaZ07pNH93RU7WD/7ZapKC1E1Kx2Gnkr2WVeFPpfbwZoP/kZF8QpsiSlknXEZ7QaeDIBj20YK33kav7OabmMvoOvoKaH314Ms+ee9nHDp3cSlZYblM/+S9MThFuqAg8EgiiJjYnEsTCxGEIwgbVq3YszZk/F5PKzKX0DZ+nWhQvr7cTsdLP3pR1YuzierTz/63vBn1D3bsXz9AWbhIhkURIP9skujQfQHFyxWDJkWIY6WaWAJeEmJt3H2Bb9hx9at/Dj3Kwyz8X9He3bu4LOPP6RbVjZDho1Grd2NWrIMvK4INF6I6FK/6oppylKUoknpJmAJrdWdm5VNbs8e+P1+CtYWsba4BIdzX5/scntYtmo1y1atpnVGOr1ysvjjiT2p9gZZuMXZ5PUZTEPHntqaIb97lLi0TPYULaXgzScZcftzxGe0bbCvEQyw/D9/ptPIs+h/yVRQVNx7ttVvXzfr36iaxpj7X8O5fSPLX32UpPbdSWrbhQ1f/pfss68iqV038p+7nXYDx2BPTmfzj5/Qpt/IiAUWQOK8kaAAwaBk84pfTzGC2ABbvJ1hJ5/C0JPHsmbpYooLVhLwNSy6G/T7WbdiGUUrl9MlO5f+U64h4fzrUefNxFw4DwJSdDdipKDj0bFarSADWnGs9CCaHqRj+3ZceNU1rFm5nJVLFmOxWBrdfdOGYrZs2kjfEwbQa9jZsLUYpawwVNdBRA8ZVIXd/gEGIZpaqD6DCoqKLc7K4IEnMGzQCVRW17Bq9TqKSzfh36+uzp7KKuYvXMxP+Uvo3KE9fXKym7w+g8UWR8/xF9f/nNl7GPEZbandWnJAcGHb0m+wp2TUZx0AJLfvBoDu97KrcAEjbn8OzR5PWrc+ZPYZxvZl35F95hV4KneR0fMEVM1KfKv2eKt3YwQD7CpcwNDfP35cP5OIbvumRQQlm1ccP3VBBhSVfkOG0j9vJKVrVrNm6SJctQ0L7pqmSdn6dZStX0ebjp3oN/Q0MideAT9+Bt/NBmdNRD5CLFMUNaqCjVEfXLBY9nWehmHQ+CWhEIem6H40PUC//ifQu/9Afv5uHptLS7BoB54CejDIqmVLKV63jsHDh9Nx5BQoXYGyrQRZ+ylKWKK+62pxFKUuc0HOARFmoUBDqD5DenorRo8YztgT89i8dTsFaxurz7CNzVu3NVqfYeEWJyUVTVOfweeoxr1nG0ltuxywrWbzeuLS27D8lenUlheT2LYLvaZcT1K7brh2b0NRVRIzO9bvn9y+O1WlhQAktetCxfrlJHfsgbdqF/EZ7Vg7829kn3UlaoT7QksUDWhjSTAYPGQ9KSGOiWlgxYCgTo+cHHr06ceOLWUU5i+gopHij7u2lvPN1nKS09PpO3AwXR+ajLniJ5S5H8KOLRH4ADEqyvqCqB+hq6plvztmBqG0DxncimNhogZ9qIrKSaeMwzPiRL798jOqKysbzWTwuF389N23ZLTOZPjIUSR36hWqx1B18Oq6IkxUCTOGXV0/HDzEElZCNLX96zN06tSJDu3aoihQtGEjq4vWs3N3Rf2+DeszJJCb1Z1L++egWduyqDxUn2HXcarPYOhBVr/7NO0HjyWxTacDtvtq91BVUsiAK6eR0fMENv/0KSvfeJyRd/wN3e9Bsyc02F+LSyBYt0xy9llXse7jf+J3VJMz8RpqytZhsccTn9GWFa/PIOh10XnkWbQ94cTj8lmOlIIkkYWbRdPqp6fJssCiyZgmGkEIBOnQoT1tz/sNjpoqCvIXsLW05IAMRkdVFQu/ncfyhT+T038Ave54AsqKQ3UZ1q9q8ubes3oHCys9eHSD1jaNa7qmcUHH1AP2+3h7LW9uqaHM7SdJUzmrbTK392yFpobOpOqAzoNrd/FzhZs0m4Xbe7ZiYrtkANY5fNy9eicV/iDXd0vnqi7pAAQMk8uXlvNM/3a0j7M2+WdtlAQXjs4vMxcktiB+NdPAEvSSZNM485zz2b1zJz98/UVdgaQDv6or9+zmi9mz6NytB0NHjERzVaGWLAW3IwKNF4BkLkSAWndu+H1+Qp2wDGtFZBmmsq8+Q3Y2uVmHqs/grq/PkNkqg9zsLO44sQdVniALtzhYutVxzPUZTMNg9bvPolg0cqf8rtF9VM1OWrfe9cUeu445h43fvI9rVzkWWzxBX8N15INeN5o9HoD49DYMuvpBAHS/j8V/v4dB1z5E0Sf/pt2AE2ndaygLnrmVjKwTsCYkH9NnOBaaRcEwwSJdQdjYbbbQWJjQmFiVQbFoYqoRRCVIRmoKI0+bQDCoU7h4IaVrCtF/cbPB5/FQsGghq5cupnuvPvS/7I9Yva5QkGHpj0225Pv1XdN5pHdbbKpCqcvPVcu20jvZTt+UuAb7eXWTP2W3pn9qHFV+nT+s2s6rm6u5vlsoUPBo0W6sisL3o7uzzunjphXb6ZVkIyvJzrMlFdyV1YqcJDvn5m/m7LbJZNo1Xt9czfg2SZELLIAEF46WatmXuWD8ooKpEL+KEUQzgrTLbMX5l13F+jWFLFu4ANXS+Em6ZVMpW7eU0atvf/oNORN2lKJsXBVa/lKEl2QuhF/dBUQgEKjLIpNjIKLDL+szDBlQV5+hqoZVaw6sz7C7opLdFYv4KX8xXTq2p19ONpPGd6d0j5sFWxwU7HASPML6DKZpsmbm3/A7qxl49QMHnaaQ3L4r1ZvWNbotMbMDpmHg3rONhNYdAHBs30RiI9MrSue9S8fh47Enp+HcsZmep1+KFpdIXGpr3BXbSQ1jcMGqKhimiUUCjWFjte67gDH2LkcpsQURDnogVPzRamHgyFEMOnEMRSuXU7RiKV53w+CooeuUrC6gZHUBHbr1oP+480k791r45iOY/wV43Y2/xzHKSrLX/31vacMtnsABwYXfdtqXzdA2TuPsdkksqvIA6bh1g693OZk1oguJmsqQtHjGZibyyQ4Hd2TZ2eoJkJeRgE1V6JpgZbs3SMAw+Xq3k/8NOTBbLaw0W2Tf/xeiP7iw30VEKHNBelJxfCl6AE0P0Lt3b7L79GXx/B8oKVrXaD0GQ9dZs2oFpcVFDBwyjC4jpqBsWgVb18tyPGGkHKQgp2g6CgqmaRIMBjENE6IrUC4EUDc6UOvqM2Q0rM+wak0Rm8sb1mcoK99GWfk2rFaNrG5dOS03h0sG9mTFttC0iZIKzyFHHOs+/ieuXeUMvu5hLFb7QfdrN+gUyn6cRUXxSjJ69mPzT59hS0wmsU0nVM1Km74jKPn6bfqcfzOObRvZvWYRw276S4PXcO7cQlVpIcPqijjGZ7ShqqQALS4R955tYV81wmpR5WsvzCwWrX4qiq7rMiYW4WfooeKPhkFu//70GjSELRvWU7g4n9rKigN237aplG2bSknPbEO/QcPpcMZFmAvnonzzMVQev2Xfp6/bxaztDryGSe9kO6NbJR72OUurvGQlhi7My9wBNEWhW8K+C/XcJBuLq0PT07KSbPxU4aZ3sp2t3iBdEqw8sGYXU7NaY1UjHGCty3KLFlEfXGgwLUI3mkGLRXOlBH1YFZW8E0czaPgIvv3ycyp27260HoPX42Hh/B9Yu7qQ4SNHkdYxF3XDUqjYGoGWxyBVOoJw27umejAYkBUjRLNw8PoMpRSuK2bXnv3qMwSCrC0uYW1xCUmJCeRm9eDS/tlo1nbklztYtKX2gPoMnqpdbM3/ElWz8uNjV9c/3uvc35PevQ8Lnr6FkXe8QFxaJomZHel30R9Z9/E/8DtrSO7QgwFX3oeqhe5E9zrnBtZ88ALfP3Il1oRkep97wwGFIYtm/YvcSdeh1N10yZpwOYXvPEXJV2/SbewF2JPTm+YXeRCaqmDIhW1YaZpWX+hC13UZE4vI2Vv8MaDTpXs3OvfMpmLXDgryF7Bzy+YDdq/avYsfv/qChKRkeg8YSNa0FzHWLkP9+gPYvOFXN+fBXm24LzeTFTVeFld5sB3mgv/DbbWsdniZ3rsNAO6gQaLW8K5JkqbiDoay5u/Kas30ot3s8evck92aZdVeEjWVjvEaf1i5HUdQ55JOaUxom/SrP8tRi4uu4IJiRvkocevWcma+/z6tMzOZOHESKXZLk83ZEaKeaiFosVFVUcF3X83B7/MdcpmXDp27MGzkKGw+VyjI4KoOSzM37arknMf+zemDevPEVVMO2G6aJk/P+pYPfl4BwAWjBnLHlLH1n2Xtlh088OZnlO7YQ492rXnk0rPp3bkdAJ8uLuSJD+di0zQeu3wieTndANi8u4o/vT6L/95xBZYIzfNSh52Fkto6Iu8dq/7+j3+SmJBA165dGTFyZP1cdyGak1DKrAGGjs/vp2DNOtYWl+JwuRrdP7NVBrk5WeT23FefYclWB65jrM/QkrRLtjH15G7EWyWTLFw2bdrIJx9/TOvMTM4++2xS46wyJhZRw1Q1Aqh4PR4K8hdQtn4d5kGmtGs2G1l9+tF34GDUPdtDdRkKFx2XLOCH1+2iZ6KNyzqnNbp93m4nD6/dzcuDO5BTN6VircPHZUvKWTq2Z/1+r5VVsajaw98HdGjwfI9ucMmScl4a2IEZ6/cwLjORk1sncM7CLczM60xamPtE9ebpqH2HhPU9DyXqE1tVVa2f66vr0oGKMDF0tICH1umpnHvx5Qw/cXQoFfwgtm3ZzCfvv8eqDZswBo3HyMmDQ6TIHi+PvvsF/bp2OOj29+YvZ97KIj669zo+nnYd3xYU8+78ZQD4gzp/+Nf7TBrej4VP3smUvBP4w7/exx/UCeoGT8/6lpl/upb7fzOBx977qv41Z7z/JfecPz5igQUg6orXxAJbXSGxwH5z14VobkzAQMVQrdjiEhkycABXXnQuF587kT65WdisDYty7a6oZP6CRbzy5rsszV9AvyQfD4/vzu/z2jOoQ3J9lfFYFMufPVI0i1Z/cyC0co8cAxE9FCOIzfCTEm9n2MmncP71v6fP0OFY7QeOh4N+P+tWLOPD1//DovUlOKdcg/nnl1BOOgOsv+7mhW7CFnfjY5UfK1z8ee0u/jagfX1gAaBrgpWgaVLm3pehVuT010+b2N8/NlZyQYcUWts1ip0++qXYSdYstLVb2HyQ921Sjfx+IynqR+gWi6V+Oplh6EhHKsJJ0QNoATdZWVlcdPV19MzthR5svOMwTYOi1QXMev8dNjn8mCOmYHbpEyo01gQ+X7Ka5Pg4RuR2O+g+s/JXcdWpebRLT6FtWgpXn5rHxwtDywItLi5DNwyuGDscm1Xj8rHDMIH8ok1Uu9y0TUsmMzWZkb26U76nCoAvl62lbVoyA7p3POh7hoUUdAw7u92OrhuhVVUi3RghjgOT0J22IBrpGa0ZMyKP311+EZNOH0e3zh0bZKuF6jNs5atvvuOVN99l2/pCTuts5fEzenLJwDb0bBUfc+fFsdZcmDt3LmeeeSbnnHMOpaWlje5TUFDAnXfeCUB5eTl5eXm/pqkthla3FCXUBRdi7R+daB6MIDYziB2dfkOGct51NzLslFNJTEk5YFfTNClbv45P33ub777/jt3DT4dHX4eJl0HSgctJ/lKFP8jnOxy4gga6aTK/wsXnOxzkZSQcsO/CSjf3FO7k2f7tOSG1YbHHBIvK+MwkXiitxK0bLKv28M1uF5PbNSySu8HpZ3GVp744ZMd4K/mVHvb4gpR5ArSPi8BcpTDczDwaUT9b64DMBelIRQQoQR+aojAsbwQDhg7n+6++YOf2baH5j7/g9/lYvOAn1q0pZNiIUbQakYO6YRnsPnAO2rFyeny88NkPvHrrpfVTHhqzYfsecju2rf85t2MbNmzfU7dtNzkd2zQYQIe27+bE3j2odnnYUVXL2vIdZLXPxOX18c8v5vPqrZcet89xzCRzIezsNhset5tAIICiKDLTWrQo+9dn6Ny5Mx3bt0NRYF1xKauLDqzPsGb9Btas31Bfn+Gy/jloVttB6zO0RMeaufDOO+9w6623cuaZZx50n/79+/PUU08da9NarP0LTQckc0FEu711GYI6PXJz6dG3Pzu2lFGYv4CKnTsO2H3X1nLmbS0nOT2dvgMG0/XhKZjL5qPMnQk7yxt9CwWFd7fWML1oN4Zp0iHOyj05rRmXmcg2b4DJCzfzyYgudIiz8s+NVTh1gxtXbqt//pC0eP41MJQBfH+vTB5Ys4sxP2z/C3t5AAAgAElEQVQk1WrhgV6ZDVaigNBylffmZGKpGzvf3rMVdxXu4PnSCq7vlk6mPfyX1opNggtHxbLfHUqZFiEiyjRRgz7iVAunnTWRmpoavp3zGR6POxQE+wVHTQ3ffDmHdh07MXzEKOydeqFuWAKOyl/dlOc//Z7zRw6gXfqBUeD9uX1+kuP3dTpJ8XG4fX5M06zb1jBymxRnx+Xzo6oKD150Bre/PBObpvHwJWfxt89+4LJThlG0bRf/+Hw+Vs3C3eedSnaHNr/68xw1RTIXws1mD02LCAaDKJIOLVoww1Tqa4r0zs2hd3ZPvH4fBWuKWPeL+gxOl5ulKwtZurKQzFYZ9MrJ5s6TulPhDtVnWNqC6zPYDrJs86HMmDGDpUuXsnHjRt566y3atGnDxo0bCQQCdOnShRkzZpCamkp+fj5//etf+fDDD5ug5c2Xtl+B6WAgGMGWCHEUTBONIASCdOjQnrbn/QZHdRUF+QsoLz2wmKOjqoqF381jef7P5PQfQK87n4Sy4lBdhvWrGuybYbPw+kGWguwQZ2XJKfvVUBhy6KzbNKuFFwa0P+Q+v3yNXsl2Zo/sesjnNDkJLhyd0LSI0D2yUHBBBrUiwgwdi+EhIzmRKb+9lM0bS1nwwzdg0mjRxx1by5n94fv0zO3FwCHjUCq3oZYsB7/nmN5+7ZYdLFi3kZn3XnfYfRPsNpxeX/3PLq+PBLsNRVFC2zy+Bvu7vD4S7aFB9che3RnZqzsA68p3Uli2nannnsr4B/7Gf++4kh1VtTzw5me8c9fVhJ1kLoSd3W6vr7mgKiq6pC6IFs4ETFRQVexxVoYOHEDe4AHsqaxm1Zp1bNhYhn+/GiS7KyrZvSCf+QsX0bVTB/pnZzN5fHc27HaRX+6kYIeT4CFq9zQ3dk3hEHWOGzVt2jTWrl3LNddcw9ixY6msrCQjIwOAZ555hpdeeompU6c2QWtbhgaZC4EAR30AhIgw1QiiEiQjLYWR4ycQDJ5G4eKFlK4pRA82DJj5PB4KFi1kzdIldOvVm/6X/RGrx4Xl6/cxl82XYqZ7adbD7xNGUR9cCN0R3m/ZHSGihR5A0wN079aFLj2uY+XiRaxeubzRqRKmabJh3VrKSkroP2gQWXmTYPNalC1rjrpzXFy8mW2VNZx6/wtAKDvBME3O/8tuZv6pYcAhq31rirbu4oRuoUjruvKdZLVvXbctk9fm5WOaZn1QpGjrLi4eM/SAtj/63pfcd+HpVDnd6KZJx1apZKYksn7rrqNq+3HTRHUsxMHF7VdzQVUVkO5YxBATQNUIAhmtWjNmZB7jThpBWfk2CtYWUVa+rX4uvGmabNqylU1btmKzWsnq3pXxOTlcMrAny7fWkl/uoKTi2ILL0cRmUQ+5itKRmDVrFrNnzyYQCOB2u+nWrdvxaVwLFRpfhP6dhYrrSnBBNFN6ABtgs1oYOGIUg04cQ9HK5RStWIrX7W64qx6kZHUBJasL6NCtB/1PvYDU865F+eZjmP8FeN2Nv0eskODC0VEtlvov7EAgKFFaEXWUoB9NCTBoyFD6DRrC/HlfsW3L5gZ3GPYKBPwsW5RP0do1DB0+grYjpqCWLMfcufGI3+/CkwZx5pA+9T+/Om8h2ypqePC3Zxyw7+S8/rw+L58xfXuioPDavHwuPSUUPBiW3RVVUfjfd4u56KTBvP/TcgDyflEg8oOfV9Cnczt6d25HUDfw+YNs2L6b7ZW1dGod3nXV60nmQtjZ7HEYdUtKhf4vU1NEbGq0PgOwdkMJq9cVs7ti39Q3fyDQoD5Dr6yeXN4/G9VqY9GWWvK31LLb1TxXYLFrKr9mhtSSJUt4++23eeedd8jIyGD27Nm89957x6+BLZCmaRjGvoKOJqaEF0TzZujYAAyD3P796TVoCFs2rKdwcT61lRUH7L5tUynbNpWSntmGfoOG0+GMizAXzg0FGip3h735UUGCC0fHYrGwN0rr8XgwUaQjFdHHNFGDXuyKyimnT8DpdPHNnM9wOR2N1mNwORx8P+9rMtu2Y/ioE0nolBuqx1Cz57BvFW+zEm/b15Ek2G3YrBoZyYks2bCZG158h6XP3A3ARScNpnxPNVMeewmAC0YN5KKTBgNg0yy8cMOFPPjmZzw961t6tGvFCzdciE3bd9FY5XTz328X89adVwKgWVTu+80Ern7uTexWjccun3jsv7NfQ4KMYRdnt9et2FOXRSYrdgjxi/oMufTJzsLr81Gwtoi1xSU4XfvuqDldbpasLGDJygLatG5FbnYWU0f3YI/Lz8JyJ8uaWX0Gm0WtL2p2LGpra0lKSiItLQ2/38/MmTOPY+tapv3HxMFgEMOUMK9oIfYWfwzodOnejc49s6nYtYOChQvYWX5gQfSq3bv48asvSEhKpveAgWRNexFj7TLUrz+AzQfWcWjRGrmZeSTmzp3LU089hd1u5+mnn6ZHjx4H7FNQUMBrr73GU089RXl5Oeeffz75+fmHbs4xtSaMVFWtr0ru8/vQTSP6Gy1il2lgCXhJTbAz+cLfsrV8Mz/Nm4thGo2mj+7euYPPPppJ9+wcBg8bg1qzK1SPwetq5MUb94ezx9T/fWhWl/rAAoRqQEw991Smnntqo8/t07kdH/zp2oO+dnpSAp/c/7sGj00a3o9Jw/sdcfuahEyLCDu73V6/7FwwqGOxIStGCFEndC6omKqKPd7KkPr6DFWsWlNE8cZNoezLOrv2VLBrTwU/LVxEl04dGJCTzZS6+gwLyp2sbgb1GeyaguVXpC6MHj2aTz75hAkTJpCens7QoUMpKCg4ji1seSwWC4qqhorr6sH6zF4hWg4TixEEI0ib1q0YM3EyXo+HgvwFlK1fh1mXQbmX2+lg6U8/snJxPtl9+9PnxodQ92wP1WUoXMwxrZfbnCjKMd/saaqVexQzynsmwzB47tmnadOmLd2792DYkEFYjeaZQihij2mxoasaq1cuZ9WSxVi0g3cAFk2j7wkD6dW3H2xdj1JWCLpUgz6AqqKOvQRFAgxhta6oiDlzvqBNZiaTJk/CHp8swQUhDkNVQA8GsFoUNpVvo/AX9Rn2t7c+Q25uDq3T01i+zUH+FgelldFZn+HCE9pySs+MSDcj5vz9xRdITk6hZ1YWwwbLmFjEAFXDb4KJwpoliykuXEnA52t0V0VR6JKdS/+Bg0jQVNS5MzHzv4FAC10e2B6P5f/eQbEc3a33GTNm8P7/s3fnwXGm953Yv8979N0AGvdFkCAJgvc14DXj8UgaW/LY0mgsWR7ZliVZRzbeJN7Ecm0ldpKyNymlXGWXKpXd1FZ5N1upctmKrLEljY6RNKORNCfv4Q0SJG4QN7rRd/d75Y9uNgASIHF099vH91MlFwn3kA8I4Onn/T2/45/+CfX19Whvb1/X5J6KylyQJAmWZSGdTvEwS2VFGGkohoZDhw9j3+EjePfNn2F06N6qTR8NXcfVSxdw9/YtHD9xCu2nPwkx+AEwOQjeES8jOwDTBDYxBo02T1WXSnF0TYfLU/kXAkRbZVqAyPZn6Nq2DZ1trQCA/oF7uHF77f4Mfq8XvT078fkjPZAUFWfHIjhXYv0Z3Cr3YDs41MxYYEPXeTKg6mDqmb4MQsLBvj4cOn0Ggzeu4+al84iFwytealkWRu70Y+ROP5o7OnHo5EfR+IkvAG/9APj5q0B00ZZPoWBcHkDXgQ0GFwo5uafkgwsAoCoqLMtCKpUCwDczKjcWJD0Fh5Dw7Ec+gkTiafzstR8gHApCWiWVKR6L4e2f/wwNTc04eeZp+Dr3ZvoxBKdtWHsJUhQ+1dpAVZRcaY+ml84DDlG5eNCfQQDYt7cX+3t3I5HM9Gfof6g/QyQWw4UPruHCB5n+DHv3LOvPMBbFpfv292dwPSYTjwpHUdVsWQTHs1OVedCXQTews7cXOw8cwtTYCK6ffQ/z01OPvHxmYhxvTIzDHwjgwJHj2P5Xn4R16W2I118Bpsdt+AQKwOUGLPPJr3uCfE7uKYvggtPlhGEYSKfTEJIAtv5vSFR82X4MPoeC3/zt38Hs1BR+8fqPYej6qv0Y5mdn8KPvfQddO3eh7+TTkKMLkO5dAhIRGxZfQmSVwQUbLM+20dIMLhBtVq4/g5DgcqvoO3oEp48fxezCAq7e6Mfd4ZFV+zO8/d45dHV24MieHrx0oBt3ZmN438b+DC6Flz12UBUVyVQSus6ySapSlgUFOqDpaG9vQ8unfheRUBDXzr6H8cFHmzlGgkG8//M3cPnsu+g9dAS9X/sbYOQO5J9+G9adqzZ8Annk8mRHGG1evif3lEVwwe32IJFIIJVKrXrTS1RWTB2KqaO1uRG/84dfxO0b13D57Htrfm+PDt7D+Mgw9h08jAN9L8CavAdp+CpQrbfHJTZyp1osL4vQtDTvy4jywAIASYEOoKGhCc89XYvnnz2D4bEJXLt1B6MTS/0ZTMvC8Ng4hsfG4VBV9Ozcgd/Y04M/OLITl7L9GYaK2J/ByeCCLRwOFfFEHLqmcXISVT3J1CFBR31dDc78+seg67+G6+few+CtGzAeCsClEglcPfc+bly8gB179+HQ5/4HqIlYpvnjpbcBs3ym9TwgXB5stXQ635N7yiS44EY0GoGmaZBkBheoMghDg2Jo2LdvP/bsO4izb/0CQwO3Ia/Sj8E0DNy4chn37vTjWN9JbDv9EsTQFeD+QPXd4ssMLthheeZCOl2hjZGIbGRaAGRHpj9DVxc629sAAP0Dd3Hj9t1H+jPcuD2AG7cH4Pd50bt7F754pAeQFZwbj+DsWBhzBe7PwJ4L9lBVByzLRDKZvXArv+chovwzNDgAOFQZR888g2O/8hxuX7mM2x9cRDIeX/lSQ8e9G9dw78Y1tO/YicPPfwY1n/oyxM++A7z9GpCMr/53lCKXe8tBxnxP7in5aREA8OPXfoTBe/dQW1eH3335ZSjpBNjgjiqKkGDIDqTSGt788Q+xMDebnWe9urr6Bpw88zRqfR5Idy8C8/eLuFh7iZYdEPtOQygOu5dSVaLRKP7Tf/5/0NTYiEOHDmHfgYMwLN6aERVS5ifMhLAMJJJJXLt5G7cGBhGLr374zfRn6EHvrm7MxtJ4byyKSxNhxLX815P+Hy/0oMZVFndUFeWHP/g+RkdGUBcI4Hdf/iykZJWXShKtRkjQIEEoDozdvYPr588ivDC/5ssDTc04eOw42nd0w3rv9UygIThbxAVvjjj1PKSX/xjC5bZ7KTllEXb2en0wjExoVmMaGFUiy4SsJ+FRgN948SV87MXfhqKqa86wDi3M4yc/eBXvvvc+Urv6YB7+COCpLfKibaKowCbGUL7++ut44YUX8NJLL2FwcHDV11y7dg1f+9rXAADj4+M4derUlpZaSRRFhZWt69N17ZFZ00SUfxYACxJMocLl9qPv2FH80Wc/hZc/+VvY17ML6kOZbjNz8/jlu+/jP//9N3Hlwlkcq03jf/voTvxXJ9pwpM0PRcrf+YllEfZwqCpMy4RpmtyHidZimVAtHYqWQFf3Drzw2c/h1z79Mlo6u1Z9eXB2Bm/95DW8+g9/j3s1rcBf/AeYX/4fga7dxV33Rrk9gFRae3FZhJy9Xk+2K26mkZjbKTNxgSqTaUA2E2iqr8Onfv/zuHenH+ffeQvSGhvHxOgIJsfHsGf/QRw6/lFgZgTS0BVAW33+b0VQHJsKMH7zm9/En/zJn+CFF15Y8zWHDh3C3/7t325ldRVLVRVY2Y1X0/RM4ItxXqKiWdGfoXGpP8PQ2ASu37qN0YnJFf0ZhkbHMTQ6DqfDgd3d2/Ebe/bgD4624NLEIs6OR7fUn0EAUGVuAHZQHQ6Y2UBvOp2GW0h56RZPVJksyKYOmDqamxrw3MdfRCKRwLWz72HkTv8jAbp4NIKL77yFK+fPoufAIez/r/8S0txkpi/D9fOlV4rsdGemqJWQ0lrNGlwud+6LmUqlAKfX5hURFdaDfgx7enZj1569uPDeOxi4eX31fgymif7rVzE4cBtHn+rDjtMvAsPXIcZvV+aBQ3FAbLCx69e//nVcvHgRQ0ND+Id/+Ac0NzdjaGgImqahq6sLX//611FbW4uzZ8/ir//6r/HP//zPBVp8+ZJlGZIkZUag6dqaWTVEVHjL+zNs37YN29rbAFjoH7iH6/0DmFsI5l6bSqdz/RlqfD709uzEF4/2AJKCs2MRnBvfeH8GpyLBtCxIzCQtOqfTCTP7QJROp+B2qbxwI1oHYepQAahuJ0489yH0Pfdh3LxwHgPXr0BLrbyU09Np3Lp8Ef1XLqOrZw8OvfQVeD79VUivvwLr7M8ArTR6TwmPb8Nn4kIri+CCw+mAyKZBp1JJQPhsXhFRcQg9DUVoOHH6DI72ncTPf/ojzExOrmiu90A6lcK5d99B/80bOHHqDOpP9UK6dxGYHbNh5QXkcG34P/nzP/9z3Lp1C1/60pfw4Q9/GAsLC6ivrwcAfOMb38Df/d3f4c/+7M/yvdKK43A4YJomEokkeJolKg0mJEB2QADY19uL/b09SCSSOP/BNVzvv7PiteFoFOcvX8X5y1fR0pTpz/Bvn+3GTCyN98eiuDgRRmId/Rm8Dhm6CbAyovi8Xh/MbDZvIplErZv9h4g2xNThAAAh4WBfHw6dPoPBG9dx89J5xMLhFS+1TBMjt/sxcrsfzR2dOHTyo2j8xBeAX34f+MX3geiiLZ9CjrfG3r9/FWURXHA6nLks6EQyyZ4LVF0sC7KehCzJ+PXf/ARCoRDe/NEPkEwmVi2XCIdCeOPHP0JbRydOnHkazo69kO5eAKLBVf7wMqQ6t/xHfPe738Wrr74KTdMQj8exY8eOra+rCjwILiSTSUhCoALzYojKlgUAQoYFGW6vig89c+qR4MJy07PzmJ6dx1vvnsX2bR04tmcPfvvATtyeieH98QhuTEVhrBFD9Kgys5ds4nK7ILLn4EQ8AdTX2bwiojJlmVBhArqBnb292HngEKZGh3Ht3PtYmJ565OUzE+N4Y2Ic/kAAB44cx/a//CSsy+9AvP4KMD1uwycAwFN6F+5lEVzIZC5kfp1MJGFBsNSXqk+2H0NDjQ8v/d7nMDJ4D+//8k0AyB00lpucGMerr/wTdu/dhyPHn4eYH4c0+AGQThZ75XklthhcuHDhAv7xH/8R3/zmN1FfX49XX30V3/rWt/K0usrmdDiQSqWRSCQgyRJMPlsQlSTLApKpFOaDIQRqa9bs2wOs3p/hhd49+NzRVlycWMTZsQiGgyvfNzwOqeRKj6uF0+nMvefH43FYYPsboi2xLCjQAU1He0c7Wj71u4iEgrh29j2MD9595OWRYBDv//wNXD77LnoPHUHv1/4GGLkD+Sf/BGtg8yMcN8VTeq0CyiK44HQ6c29iqXQKpmWhtKpLiIoo24+hu3s7tu/8Cq6cP4ubV69AVh79qbAsCwO3bmL43l0cOnocu0+9CIzehBi7BZhlOhxb3VoKaDgchs/nQ11dHdLpNF555ZU8LazyORwOJBIJpNPpTK01Hy6ISpaqKtixrQP9A4OwYKHG54Pf5101GP3Aiv4Mfh96d+/Cl471wBQyzo5HcG4sjPm4Bo8qM4nUJi7XUmlgMpmAYVnlcZgnKgOSqUOCjvq6Gpz59Y9B15/H9XPvY/DWDRi6vuK1qUQCV8+9jxsXL2DH3n049Id/CjURyzR/vPR2Uc7ZwuMv+N+xUWWxHzkczlz6XTrF4AIRAEh6GpLQcKyvDweP9+GtN36MybGxVZs+auk0Lp17H3du3UTfqdNoOv0i5HuXYU0PF3/hW6VsLbjw7LPP4nvf+x4+9rGPIRAIoK+vD9euFTnSXKacLifMYKYYQtM0QN56iQoR5Z8QgKo68OXf/wzC0Sj679zD2+cuYWJqGkJIqK+rgdv1+P414UgU5y9fwfnLV9Da1IjePbvxb391B+bjBhaSBps52sTlXBZcSKWYQUZUCIYGBwCHKuPomWdw7Feew+0rl3H7g4tIxuMrX2rouHfjGu7duIaO7p049PxnUPOpL0P87DvA268Byfjqf0c++Eqv54KwyqBozjAM/F//5zfQ1NyC9o4OPHPmDBxmaXTpJCoJkgxDdiASieDN136IWDTy2DTY5tY2nDzzDNySCWngAhCeK+Jit0Z67uUtl0bQ5vz09ddxu/8OAoE6fOITH4fTU8PkBaISJItMs8Xlz/+WZWF2fgFXb/Tj3QuXEI7GoCoK6gN1UNc5ymxqehaf+8wnsXvXLqiyBFligKHYUqkU/uP//e/R1NyCltZWPPvMMzwTExWakKBBglAcGLt7B9fPn0V4YX7Nl9c3t+Dg0WNo29EN673XM4GG4GzelyV/4xUI58YbnRdSWWQuyLIMVc00EkunUmB1GdFDsv0Y6rwufOIzL2NibBTvvPkGLNNcNQV2ZmoS3/+Xb6O7pxfHTzwHKTQF6d5lIFXA6Gq+yKrdK6hatTU10LNpgYlEEi5vDeuuicqEEALNjQ34teeewUeePYOR8fu4dPUGLly5Bk034HY5n9ifQTcNJFMpuFTmj9rF4XAAQsA0TaTY5JyoOB40f9QMdHXvwLZdPZifnsK1s+9henz0kZcvzEzjlz95DR6/H/uOHMPuv/gPMG9ehPTTV4CxR/s4bIokb7lUuBDKIrgAZLrjGoaBVCoFIQmwTTnRKgwdiqGjq7MDHV/4Eq5fvohrly5Allf/UR8auI2xoXs4cOQYek9+HBi/DTF6AzD0VV9vO1kBC/3t4/P5YGU333g8hnqb10NEqxPi8c+ckiShu6sT3V2d+PhHP4y7QyN4/+IHS/0Z/D74vY/2ZxBCwOVk5pidhBDwuD0wDAPJZAqSLANl2kKJqPxYkE0dMHU0NzXguY+/iEQigWvvv4uRgduwzJUPqPFIBBff/iWunHsfPQcOYf8f/yWkufuQf/ptWNfPY0s3NL4aQNcAR2ntyWUTXHC7PUuNxCRGzIkeR+hpKNBw+MhR7D9yDO/87A2MDQ9CWSX1Vdd1XLl4HgP9t/DUyVNoO/1JiHuXgalBG1b+BA43YJqZaC0Vncvlzs3qiUZjgGUC4KB7olKzkbtsp8OBA709ONDbg3A0ipu37+Ld86v3Z5AYXCgJXq8XiWQSqVRyzcsDIiosYepQAahuJ0586MPo+9BHcPPCeQxc+wBaemWpkp5O49bli+i/chldPXtw6KUvw/Ppr0J6/RVYZ38GaJsobfLXZi8DS2tPLpsdyevxIBqNQNO0TJSWiJ7AgqSn4BASfvUjzyOeeBpvvvZDhBeDqwbo4rEo3nrzDTQ0NePU08/A27kX0t0LQGjGhrWvweHaWpSXtsTtduWuQxOJBEzLBASDC0SVosbnw+mnjuLU8SOYmZvHtZu38c75S5gPhqAqKnTDgNNRemm41cbr8yESjcKyLBi6DgUCzOojsompwwEAQsLBvj4cOn0Ggzeu4+al84iFwyteapkmRm73Y+R2P5o7OnHo5EfR+IkvAL/8PvCL7wPRxXX/tcJXV5Jn4rIJLrg9Hui6wY2UaKMsE7KehN+p4jc/9TuYmZzEL1//MQzDWLUfw/zsDH743X/B9p278NSpZyBH5iHduwQkojYs/iGO0mpaU20eHoFmmSY4uoeo9Gy1DF8IgZamRrQ814gP/8ppjIzfx+VrNzEwNIwavy8/i6RN8/l8ubF4aS0NRYiSfMggqioP+jLoBnb29mLngUO49v47uHnx/Kovn5kYxxsT46gJ1OPA0WPo+quXYF16G+L1V4Dp8Sf/ff5a4DE9cuxSNsEFj8cLw8gUlWmaxo2UaKNMHYqpo62lCb/z+T9C/7Wr+OD8+2uWGY0M3sP4yDD2HTqC/X2/Cdy/CzF8DTC0Ii98iXC4eFNuI7fbnRsLnEgkGeIlKlH5bPEnyzJ2bt+Gndu3wbKsVYPSVFw+nz/XXDeVTMHjcXAzJioVlgUFOmBJcHm9iIRC8NXWrrl3hoMLeO/NN3Dp/XfRe+gIer/2N8Dw7UxfhoHHjEr312Z7kZWWsjmle70eGNkmc0l2xyXaNGFoUNIJ7D9wAC9/8avY1r0zd0h5mGEYuP7BJXzv29/CmCbDOvNJoKPHvp8/hwtgWZRtnE4nRLZLeTKZyDTXJaKqwcBCafD5fDCzjeN4JiYqTZYQaOnsQk1dHWbGxxCcncn93K4mlUjg6rn38c//5T/h8tQ8kn/4pzD/p38P0ffcqr3GRE09oJTeBLWyCS4sbyQWi0V5e0m0JZl+DKqRwtPPPodPf+4LqK2rz2UHPSyZiOO9X/4CP/3RDxCq64J54uNAfVuR1wzA+Wj3cioeIQQ8nkyX8kQiCYWBHiKionM6nbngbiIR55mYqAQJIaG+uQW/92/+DJ/97/4U23t6MXd/AnOTk9D1tbOADUPH3etX8Z2//3/x7qVLCD3/GVj/+38Bnv8U4PIsvTDQWJJn4tLLpViDw+nIRWYjkSjQ0mzziogqQLYfg1eR8bFPvoT52Vn84ievQdPSq25Ywfl5/PgHr6Jz+w70nToDNRmGdPciEA+v8ocXwPJNlWzh8/kQi8agqkauRIKISkfpHTUp31wuF6RsQCEWi8PKXb8RUcnI/owKIdC+oxvtX/wKgrMzuPLOW7j6/tswDAN1DU1wuNbuJzYxNIiJoUHUN7fg4NGTaHvhZVjv/hTize8CtaU5ELxsggtOhxOSeJC5EINuWuWzeKJSZxpQzASaGwL49Oc+j4H+W7jw7tuQ1mgUMz4yjPtjo+g9cBAHj38MmB6GNHwV0FIFXaZwuAv659OT+f0+LIZCANxIpdKQHW6W+hKVkBK8yKI8c7pcubZjqVQShmnyTExUalbZjANNzfjQS5/Gyec/ipsXz+H8z36K4NwM/LUBePz+Nf+ohZlp/PInr8Hj96N7dw8O/6//EaIEmzkCZVQW4XQ6c7dk8XgcJm/MiPJOGBrkdBy9e/bgs3/0VXT39EI3Vu/HYCWV7scAACAASURBVJombl27iu99+//DSNyAdepFYNvewqZnclqE7WpqanI9OpKppM2rIaKHMbZQ+VwuV+5MnEwmsXYVNxHZ5jHnYY/fj74PPY+v/M//Di/8/hegOhyYHhvF4sL8Y7NC45EIfvGD72NhYQFCLc2xwGUT6HS5l24s4/F4ZvTG6uXhRLRFQk9BEQKnzjyNoydO4hc/+RFmp6YgK49uGalkEufeeRv9N27g5OkzCJzqzZRKzK1jjM5GKaW5kVYTv98PXc9svol4Ar6aAAf3EJUQZi5UPpfLCct60NAxBYaUiMqT6nBg3/E+9B49jvF7Azj3xk8wevcOFNWBusYmyKv0trJgweku3UzesgkuuN1umKYJy7IQj8cz4/MYXCAqHMuCpCfhlmT82m+9iFAwiJ+/9gOkUqlV+zGEQ0G8/toP0da5DSdPPw1H515Idy8A0VB+1iNESY7cqTZejzf361gsBna/ISotAgwwVDpFUSHLUnZyTzKTHs30BaLSscFNWJIkdPX0oqunF7P3J3D5rZ/j5oVzgADqGpuhOpYu1yyrtIMLZVMWoSgK3G43DMNAKpWExC7lRMVhGlC0BBpqfXjp9/4Qp5/90GNTtibHx/C9V76FK7fvwTz66zB7T+ennEF1AiYjinZzu125LuXxeCx3e0ZEpYGBhcqXmdzjha7riMdjkBl4JyotWygRbmrvwEdf/gN8+S/+Eic/8lFEQyHMjI8hGY/BNAxIkgTV4czjYvOrbIILAOCvqYGmabAsC1o6zXdQoiIShg5Fi2Pnzm68/MWvoGffgVzt/cMsy8KdWzfwnW/9IwZDCVinXoS1/UCmnGmzVBfAB1nbuVxL0fJEIgmTAR+iksKTUXXwer0wdB26rsO0TPArT1RChAC22O7aXxfA07/xW/jK//JXeP5TvwvTMDA9PgqP31+SIygfKKtQZ01NLcLhMNxuN5LJBJwuFbB4sCUqpgf9GJ46cRKHn+rDL1//CaYmxla9OdHSaVw8+x7u3LqJvlOn0Xjqk5DuXQJmRjb+FztcW92nKQ/c7uWNxBJgwwUiouLzer1YXFwEkOl/43dIzO4jKhVCQr4Cfi63B4ef/hUcOHkaw7dvIZ0s7WbaZZW5UFdXB03TAGTm+ha0Kz0RrS3bj8EJAx/52Av4+O98Fi63B6a5emZBJLyIN3/6Y/zi528i1nkA5vGPAf6GDf2VwulmtlIJeNCl3LIsJBJJfkmIiGzg8/lz05xisRjfH4lKSQF+HmVFwa4Dh7DvqRN5/7PzqayezuvqamFk07AjkQg3UiK7mQZkLYGAz4NPvvz7cDpdCIeCa/ZkmJm8jx/8yyu4eP0WjMMfgrnvacDpWd/f5fICEnut2E1VVaiqCtM0kUgkIJfonGWiasRTUfXw+f250sRwJMwLN6JSIqSqfU4tq53I4/Hmakyi0QgMZuMSlQZDgywJfOSFj6M2UI/pyQkk4vFVX2pZFgbv9OM73/omBmbDsE5+HNaOw4D0hCottz/TEZts5/NmGomlUilI/JoQlYwqPctWJb/fn5sQEQlHYLBEjah0VPFlWFmdCt0e91JwIRZjcIGolAiBhuZmvPxHX8VvffqzMA0DM5P3c6VMD9M1DR9cOIfv/8u3MSn5YJ1+EWjtXvuPd/sLtXLaIJ/fB13XYVkWkskUb0uJSgR/FquH1+vNTe6JxWIw2O+YqHRUcSZRWTV09Hg8eNDRLRaNMkRPVFIyP4+SJKH3wEF07+7BlQtn8f4vfw5YFgKNjZBWieTGo1G89bPX0djcgpNnnoa3cy+kgQvA4uzKF7q8RfgcaD38Pj9mZjJfn1gshlqnm30diUqAEDwaVQuvz5f7dSwWy0xjYj9HIrJZWYVVPB5PrpFYLBaDrKh2L4mIgFUjtA6nEyee+VV88V//G+w9eASzU1MILSys2Y9hbmYaP/zuv+D85avQ9j8L88CzgMu37A90FWr1tEH+mhroWqbWdzG8yNtSohJRVoc62hKvxwMrO545FotCVsrqvpCoclVx1gJQZu9DquqA6nDAMAxompZ9SOGxlsh2j5nn66+txa+/+BJ+/6t/jMbmFkzfn0A8Flvzjxq+N4Dvfuub6L8/C+vEb8LceRRQXYBcvfVrpabG74eRHXkWXlyExZHARCWBWQvVw+F0QlUzZ+J0Og2eh4lKRJX3oiq7z762pjZXw51MJPhOSlQK1jHPt6WtHZ/5wpfwyc9+DkJkJkek06lVX2sYOq5dvoRXX/kWBmMmpGd+GzD4AFsqPF4PpFxz3ShMfm2IiIpKCIGa2hpo6TSAB2fisjvWE1WeKv85LLvPvi4QyG2ksVi06qNDRCVhnT+HQgjs6t2Lz//xn+BXP/obiIbDmJ2egrHGw2ksGsGPX/0uICuZ/1FJ8Pt8ucBuNBpljJeIyAZ1dQGksxduub4LRGQvIVf15XfZ7UL19fW5jTQc5lxfopKwwXm+qqri+Kmn8Uf/7X+Pw8f7MD8zjdDC/CP9GLS0Bn9tLYQQuUkxZD+fz5f7WkWjMSgM/BDZjjtk9amvr89duC2GF3kmJioFVR7kK7vPvq4uAPNBrW8kwnGURKVgk/N8vT4/PvzCx/G5f/XfoLW9EzOT9xGLRHL/f01Lo6Y2kK9VUp643W5IQoJpmtA0LbcnE5F9GH+tPnWBwIr+NzwTE5UABhfKi9fnhZSNzMaiMRgmd1Ii223xVNvY3ILf/oPP41N/8AWoDgem708gnUpBS2uoC9TnaZGUL0II1NbVZpuIAfF4gremRDbjz2D18XqWzsSRaJTBBaKSUN27cfkFF7yrzPUlIpttfSMVQmD7rt343L/613j+t15EPBZDcH4WgQYGF0pRfaA+F1yIRCO8NSWymRDMXqg2Xp839+toJALBMzGRvViahLIrlPV5vbm5vtFYFLKiAsbqHeeJqAjyvJEqiorDT53A7r37ceXiOWzf2ZPXP5/yo6GxAUNDQwCAxdAiWlraUIbxaqKKwbhC9fF6l/e/yZ6J9aTNqyKqYkJCZjR79e7IZRdccDidUBQ1010+nYZhGJCFACzmghHZQirMRurxenHmVz+c1z+T8qc+EICZDfSGw+FM3S9vzYhsw6yF6uNyuSArcm7ikpZOw8kzMZF9pCePZq90ZXcSzMz1rc11x41GwpmRH0RkD8GNtBr5fL7cBI9IJMLDLJHNuAtXHyEEAnWBXIlaLBbjmZjIThucnlaJyi64AACBwNJc34WFIG/LiOwkVfc832rlW1brGw6Hocg80BIRFVugviEXXAiHF3kmJrLTJqenVZKy3IGWz/UNhoLQTZsXRFTNuJFWJZ/PB9M0YVkWUqkUMqUxRGQHifHdqtXY1Ih0OtN7LBRaBIeoEdmIDR3LM7hQFwjk6ssWFxfB2AKRjbiRViVVVeFxe6DrOgAgFoszLZvIJvzZq16BurpcbDcSjUBniRqRfZjJW57BhZqaWkjZtK/w4mKmOy4RFR830aoWqA8sS8cN89uByCYcQ1m9vD5/7osfjUTZc4HILtyEAZRpcKG2tjY3eieZTGZ/zS8oUdEJGUyHr15NjY1IpTLBhYXgAmAxj4zIDiyLqF5+vx8P3ocjkQgUpewGwRFVBmbyAijT4ILX64UsL43eiUYjbGBDZAeO3KlqTU1N0PVMc91IOALTNGxeEVF14i5cvTweDwQA0zSh6xo0TeNDDpEd+HMHoEyDC5Ikob6+HulUpoFNMBhiUzkiO3BSRFWrqamBeFCiFg5DMIuFiKioZFmGv2ZpRPviIidGENmCP3cAyjS4AADNLS1IZoMLCwsLMHimJSo+BvWqmr/Gn/t1JBKBynRcoqJjSQQ1NCyNo5ybn4NZvsd7ovLFCzcA5RxcaG6BrmXScRcXFxlcILIDU8Cqmt/ng2VZsCwLuq7nJkcQUfHwKEuNy4ILwYUgDE6MICo+nokBlHFwoS5QB5GNDi0uLkKSeWNGVFw80lY7VVXh8/kyNb4AotEob1GJikwIi5dlVS5Q3wDTyDTUDYWCzCoksgODCwDKOLhQW1uLB91xE4l4NtDAd1eiomFtGSGTjpvKlqjNLyxwFyYqMomRhapXW1sLkY3shsNhjmgnKjYGFnLK9l/C5/MDEDDNTKQ2FovyYYeomHgzQgCam5qQyqbjzs/NwTQ0m1dEVF0YWqC6QB2s7Chgy7IQj8X4Hk1UTBJHsz9Qtk/jsiwjsHxiRCjEqBFRMQk2rqFM5oKRTccNBoPgmysRUXG53R44na5ciVowuMAzMVERWZIMhnozynrnaW5uXpoYMb8Ag19UouJhphABqKnxQ8qm44ZCi5wYQVRE7HFCACCEQEtrC5LJJABgbm6eZ2KiIhKcFJFT1k8HLS2t0LLBBU6MICoyplwSAL/fDyvbmdw0TcTjcR5piYqEP2v0QFtbB1LZ4EIoFOSZmKiYeCbOKevgQl2gLhclWgwvQpL5hSUqDh5pKcPn80GWZBiGAQBYWFjgbSpRkXBSBD3Q2NiIBxMoQ6EQJDZ1JCoObsIrlHVwobamNveME4/FMikpRFR4kgTW1hMASJKEpqamXDru7OwsLNOweVVE1YGTIuiBzIj2B1PUEtmMMn5/EBWcYDPH5co6uOCvqQGsTCouu+MSFZGQwEMLPdDZ2YFENriwsBBkcIGoSLgL0wO1tXWwLOTK1CLhMM/EREXAZo4rlXVwQVEU1NXVQcuOQVtc5MQIomKw2LiGlmlpacmNBQ6FglAUHmiJiIpJVVXU1dUhle1FNj8/x8bLRMUg80y8XNnvOk3LJkbMzy/AZOSIqOBYgkTLBQJ1uffVdFqDpmnciYkKjL1N6GEtrW25po7zCwvQTKZqExUaz8QrlX1wobW1DencxIgQdIsbKVHB8TaElqmry6TjPsheCIZCDOITFRh/xOhhbW2tSKWzZ+JQCBazeYmKgLvxcmW/6wQCgdyvFxYWICkOG1dDVAWEADdSWk5VVdQH6pFKZUrUZmdmAMu0eVVElU0IZuLSSoH6eojsN0UoFIKicmIEUUFJbOb4sLIPLtTU1ubeXOPxOEzD4LstUSEx/YtW0d7ehmQyASDT1NE0dJtXRFTZWBZBD6urC+SecwzDQCqZYi8yokJiM8dHlP2OU1NTA9Oyct1xFxYWAEmxeVVElcsSDC7Qo9ra2pDWNABAMBiEIpf92wtRSeNxlh7m8/mgKAoMIzOxJxQK8UKAqIDY4PxRZX/6U1UVNf4apLMTI6amp2DwLZeocGSFGyk9or4+ACnbiyMej4Ptb4gKhzswrUaSJDQ2NSGZbeo4NzfHRudEBcRmjo8q++ACkJkYkRu9MzcHg4daooLhRkqrCQQCsMylLLLFxUWmbRMVCH+2aC1tbUsTI4KhIBudExUSy44eURH/Ip2dnUujd+YXIKts6khUENxEaQ1utxtenxdatjRibm4Wgk0diQpCEhYTyGhVzS0tS2URwSCEzFJhooLgmXhVFfGv0tTUnMsR1HUt01SMX3Ci/GPWAj1GW2srEssCvQabOhIVhMTIAq2hri6QmxgRjUYh8X2bqDD4s7WqingCr29oWJGOOzc7l6kLJ6K8YuMaepyOjo5ciVowGOQDEBFRkQXq6mBZ5lKJWijERudEBWAxuLCqiggueDwe1NQsNXWcnpmGbrLGjCjvGLSjx2hsbMjFnsLhMGROjCDKO/ZboMdxulzwen25ErXJyUmYzOYlyjvBC7dVVcxu07ltGxLxOABgfm6e4/KICkDwgEKPEQgEclMiLMtCNBpjn3KiPBPg5Qk9XktLS25ixMzsDHR+yxDlHzMXVlUxTwqdnZ3Q0pkobSgUhKTwhpUoryQZ4KGWHsPn80FVVeh6ptfC/Pwcb1mJ8kwSvCyjx2tta8+VqM3NzrLROVG+cRNeU8UEFxqbmnI9HC3LQiQcZkSJKI8y2UDcTGltQgi0Lrsxm5ubg8mmjkR5xV4m9CSNjY25DBdN05BMJHgmJson9jFZU8UEFwKBelgQMM3M6LPpmWmY3EiJ8kdmbRk9WUdnBxKJpeACU7iJ8oc7MK1HfUN9rkQNAKanpxlcIMojNnNcW8UEF1RVRVNTU+7GbHZ2lk0difKJzRxpHZqbmmBlAwqh0CIk1kUQ5Q1/nGg9ampq4XI5c00dp6enoPFMTJQ/ssoLtzVUTHABALq6upY1dZyDJKs2r4ioUggI3pnROgQCSzPWLcvC/PwCH4iI8kTA4nmWnkgIgW3buhDPnolnZ2cheCYmyhORO+fQoyoquNDW1g7TyJRFxGKxzIxffvGJtk5mM0dan9raWgixVKI2MTEByzRsXhVRZZAq6tRGhbR9RzdSqUw2bzQahckzMVF+8Ez8WBX1NlXf0LCiIDEYXGCNGVEesJkjrZcsy2hsbFgagzYzA1gMLhDlAzPIaL2ampsgLRsfPT83xyZ0RHnAM/HjVVRwoba2Foqi5MagTU1Pw6ysT5HIHrLCGw9at65tXYjHEwCAhYUFKDKDvERbxfIi2oj6+oYVWWSTk5Mw+EBEtHU8Ez9WRT15S5KE9o52JBKZQ+383Bx0Zq0QbZlgBhBtQGdnB0wrc6C1LAvBYJAPRkRbxMkrtBGKoqC1tW1F3wUGF4jygGfix6qo4AIAbOvanpnnC2B+fh6y6rB5RURlTlTcNkEF1tzcDMuyMn1vANy/fx9g3wWiLZEEL8toY7Z370AyG1wIBhcgK2zqSLQlkswQ3RNU3FNDc3NzrgwmnU4jnUrx4YhoKyQ2rqGN8Xq9qKutRSqdBgBMT8+wqSPRFkmMLNAGtbW25SJSpmkivLjIvgtEW2Dx5+eJKu6pu6GhEVh2YzY3N8v0FaItsCSZATrasO7ubsRjMQCZLDJF4T5MtFkMK9BmNDY1wTTN3Jl4cmoSJkeOEG1a5kzMHflxKm6H8Xg88Hp90LTMjdn9+5PQeOlKtHmcjU2bsG3bNuhGJlvBMAyEw2H2XSDaJJ5laTPcbjcCgQBSqRSAzPQe3bR5UURlTMjMXHiSigsuCCHQuW1brlP51NQkhMK+C0SbIgQET7W0Cc3NTSt+PzFxH7B4qiXaDImlabRJ23fsQDyeySKbm51lLzKizWK/hXWpuOACAHR2bsv0WgAQi8WgpdNM6ybaDEkB+y3QZvj9fng9XqRzfRemYRq6zasiKk+SxOwF2pyOzk4YeiaLLJ1OI5VM8kxMtAkWy+zXpSJ3l8amJkjLasruT96HyQYcRBtmst8CbZIQAjt2bEcs23dhbm4OKvsuEG2K4H0ZbVJTU/OK38/MTANM7SbaMPZbWJ+KfGpoaKiHZWU64wLAxMQEdF6+Em2YYL8F2oLt27dD0zPZCrquIxqN8RGJaIPYq4S2ora2Fg6HA5qmAQCmpqagmTwUE20Uz8TrU5HBBVV1oLmlCYlEpu/C9PQ0a8yINkowD5e25uG+C5OTkxBg3wWijRAwuRXTpgkhsK1rO+LxOABgdnaWTemINkpIvBxZp4oMLgDA7t17cmPQtHQa0WiEIymJNsCSFG6ktCV1dXVwOp0rbszYd4FoY2SmLtAWbd++HalUEgAQiURgWeDlAdFGMCC3bhUbXOjo7FwxGHp8bBymYHCBaL1YW0ZbJYTA9u1diC27MWPfBaL1EwCDvLRlTc3NkJa9n09PT2UbNhPRepiCZ+L1qtjgQnNzM2RJgpGdsz45OQmdb9FE6yYU1pbR1nXv2IFUKjMxIp1OI5FIcCcmWqdM0gJ/YmhrGhoaAIhcL7LR0TFoFr+viNZLKAzGrVfFBhcURUHntq5lncpnISsK+CZNtA6SDMERlJQHzc0tK4L9k5NTkNh3gWid2G+Btk5VVbS0tiKRyGSRTU7eh6TyAoFoXYTgxJ4NqNjgAgDs2r0bqUSmxsw0TSzMzwMyU3KJniQzy5cbKW1dfX0AqqpCz06NmJqahMG+C0TrorDfAuVJd3c3EvFMo/NUKoVoNMpeZETrISkAL9zWraKDC+1t7Suej8bGxqFX9qdMlBeWpLC2jPJCkiR0bduW67swMzMLhX0XiJ5ILPu/RFvV2toGy1p6QBobHYXBXmRET2RKSmaCGq1LRf9LBerrV3Qqn5yahMWNlOiJOKaK8qm7ewdSyRQAIJlMIhFn3wWiJ5EEb8oof5pbWgAg13dhYmICJh+YiJ6IPcg2pqJ3FUmSsHPX7kzqF4DFUCiT1MIbWaK1yRxBSfnV0tK6Iug/MjICYRn2LYioDAhYPK5Q3rhcLrS3tyOezSJbWFjI3Mbym4xobZLMM/EGVXRwAQC6d3ZDT2u5309PcfwO0eNwZCvlW0NDPSRJzk3vGR8fByw2dSR6HJn9FijP9vT2Ih7PNDq3LAtTk5OAzFtZorXwTLxxFR9caG1tgwUrV2c2PjEOjZmGRGuTVd5kUF7JsozOjo7cjdn8/DwAi7cBRGvgCEoqhI7OzhVd70fHRqExzku0Np6JN6zigwt+vx91gTqkUpl636nJKUiKw+ZVEZUoISCkit8WyAbd3d1IJJO5309M3IdgTTnRqgQze6gA6usb4HK7kU6nAQBTk5OQVJ6JiVYlBASnDG5YVTxF7N69B7FYpu9CIhHPBBrYxIboURL7LVBhtLe3rfj96OgILENb49VE1U1mKTwVgCRJ2LNnD6KRCIDsSMpImCMpiVbDM/GmVMUTdldXF0xj6RZg4v4ETG6kRI8wJJknWiqIpqamldN7Jqeg8EaA6BECgOA+TAXSvXNnrv8NAIxwJCXRqgzBM/FmVEVwoeWh8Tv3JyagW/xmIXqYxHE7VCCSJGFvby/C4cyNmWEYmJubB3vWEa2UGUHJHwwqjLbWTBbZ0pn4PkdSEq1CUnkm3oyq2E2cLhda29qQSGSaiU1Pz0BmjRnRSkICD7RUSDt37oRhLt2YDQ8PszSC6CHCMnlZRgXjdLnQ3tGRmxqxsDAPQPCGlmg5ZrhvWlUEFwBg9+4exOMJAICuawgFg4DMkZRED5isLaMCa29vgySJXEruxMQEZDYQJVpBlvkzQYW1p7cXieyZGAAmOZKSaAVTyCsmq9D6Vc07WEdHB2AtdSYfGhqCblXNp0/0ZBy3QwXmcDiwvWs7orHMjVkikUA8HmNpBFEWR1BSMXR2blvx+zGOpCRaSXHwTLxJVfN03dTcDFmWczdm4+NjEKwvJ8oQEgRvy6gIent7kVw2knJ4ZARYVipBVNU4gpKKoL6+Hm6PJzeScpIjKYmWCIlNdbegap4mZFnG9h07EItmRlLG43FEY1HW1BABMCWmf1FxdG7rhBACVjaTbHxsHAAfqIgAQJEEL8uo4IQQ2LNnDyLZkZTpdBqRcBiQWC5MZEoKgwtbUDXBBQDYtWsXUqllN2ZDwxy/QwTAkhSmf1FR+H0+NDY2IpHI1PsGg0FYpsnQFlU9SYAVEVQ03d07YS4bSTk6OgqDUyOIYHEs+5ZU1S7S1t4BYOnGbHR0NPNQRVTVBCQ2N6Ui2rdvb67vAgCMj09AYvYCVTvTYAYZFU1rWxsgRG4k5cTEBEdSEgmeibeqqnaRuro6BAKBXL1vJBJGKp1iaQRVN/YeoSLb3tW14vejo6MwDd2m1RCVBkVmSQQVj9PpREdHB2LZQG8wuAALyI6lJqpSnJqyZVW1gwghsP/AAUSzfRcAlkYQ6RAQHAdIRdTQ0ACP251rJjY1NQVZ4T5M1UsSyGVVEhVLb+9eJBLx3O/HRsdgMqOXqpgOiWfiLaq6f73tO7pXjKQcHRuFyeACVTFZYYdoKi5JktDb24tIJBPoNU0Ts7OzHElJVcsydAjeGFORdXR2rijFGRoahFF9jwZEObLKzIWtqrodpLGxEV6fF6lUCgAQXFjI1JvxTZ2qkayCd2Vkh507u2EsG0E5MjwMy9BsXBGRfVRFgsToGhVZIBCA1+tFOp05E8/OzrI0gqqXrICH4q2rut1DCIH9+w9kRu5kDY8MMw2MqpIOCRLTv8gGbW1tkCQJRrZb+cTEfSgyvxep+kgCME2eaKn4hBDo2bMHkXBmJKVlWRgZGYbJXmRUhXTILInIg6r8F+zeuROWtdSZfHhoiON3qCrJKksiyB6qqmJnd3euB04ymUQkEmFpBFUdy9Ahy3yYI3t0d+/MTYwAgKGhIfYio6rEM3F+VOUTdXNzC5xOFzQtk4I7Pz8Pw2BpBFUZWWUDMbLVnj17ciVqAHD37j1YnBpBVUZVJE6JINu0tbdBluVcFtnc3Fwmk4ZnYqomsgqTZ+K8qMqdQ5Zl7N23b0VpxNDwENPAqKpokCDxtoxs1NHRDkDkglwjIyOQZT5lUfVgSQTZTVUd6OnZg3B4Mfex4eEhlgtTVdEgMYMsT6oyuAAAu3f35KK0wIORlNxIqVoIpn+R7Xw+H5pbmhCPZ0ahJZNJLCwssDSCqoZlaFA4hpVstnffPujaUtbYEMe0UzURArLCKRH5UrXBhda2NqiqCl3PbKbB4ELm18xeoGogK7CW1VgS2WXfvn2IxpbmrN8duMupEVQ1VAYWqAS0d3RAUZTcmXhhYT5zAcfSCKoCpqSsmF5FW1O1u4aiKOjduxfhxaU0sMHBQUZqqSpokCArzNQh+3Vt64KAlSuNGBsbg8ypEVQFJAHW+FJJUFU1cyZeVhoxODQEg6URVAUMoUBlNm/eVPUJrrd378rSiJFhWMxcoIrHkggqHQ0N9aitq0UymQQA6LqOyfuTkAQfuqiyWYYGhTW+VCL29PbmMhcAYGjwHiwGF6jSSTIEO+rmVVUHF9ra2+FwOHJTIxZDIaTSaZZGUEWzWBJBJUQIgSOHjyASjeQ+du8eSyOo8rEkgkpJe3sHHOqyM/HiIhKJBM/EVNF0SOC4nvyq6uCCLMvYt38/wsumRgzeG4TBGjOqYDpLIqjE7N69C7CWpkbcvz8JSQjw7Z4qFadEUKlRFAV79+1HJLJ0Jh4YGMg8fBFVKKE6oPBMnFdVv2P07NkDc1lpxODQICyZKeNUoYTEjrhUf9AOCgAAIABJREFUcmpra9HS2oJYLAYAsCwLIyMjEGCGDVUmTomgUrRnzx7o+rJy4eFhCIVnYqpQkgLT4Dkj36o+uNDa2gan04l0Og0AiEWjCAYXAJkPYFR5DCHnboeJSsmRw4cRiy9Njbh3bxCw2L2ZKhNLIqgUtbW3w+V05kojkskEFhZ4JqbKpEFAZt+bvKv64IIsy9h/4CAiy0oj+m/1Q+M/DVUixcGSCCpJ3d07IISAme0HMjc3By2tsTSCKo4kwCAvlaQHZ+Llk9QGBu5As7gTU+WRHU5IDC7kHZ+gAfTs6YG5bL7pxMQ4LCFxvi9VFlmFtqwTNFEp8Xg86O7egUhkqbHjnTt3AJPfs1RhDI23ZVSyevfuXXEmHhsbg1BUgKFeqiSyumI6CuUPn54BtLS0wu3xIJ1OAQBM08S9u3dhsEMuVZC0CTatoZJ26OBBJFOp3O+HhoYgyzzQUuUQACSJRy8qXc3NzaiprUUykQAAGIaB+xMTMFkaQRUkbQmoHMteEHyHQ+aN/tChwwgvLu+QewcWN1KqFEKCpKgMLlBJ27ZtGxRFyd0mJBIJzM3NQWJ8gSqFqa24FSYqNUIIHDlybEUW2d27AzCYuUCVQgjIqgOCIygLgsGFrL1798E0zVwdZDQaRSgYYhMbqgiGkJFadiNMVIocDgf27t27Yjzwndt3YBmajasiyh9FluBw8LaMStuu3bsAWLkz8fT0NEwLLBemimBKyopJgZRf3CWyAvX16Ny2bUWk9lb/LTZ2pIpgySo8Xq/dyyB6ogP7962og5yYmIAkWO1L5U8SFhKJpN3LIHqi2to6tLa1IxqNAsg0IO3v74cuMfuRyp8hFKgM8hYMn5yXOXb8eK7GDAAmxsczUVpGaqmcySo0Lc30LyoLbW1t8Pn9SCYzD2GmaWJoaAgCnEVN5c0yNDgczIak8nDkyFEkEkvjge/eHYCQ2diRypwk8zxcYHxqXqarazucTifS6TSAbGPHe2zsSOUtbQKywgMtlQdJknDs6BGEI8t74NyFsBhcoPIlAFimyZIIKhvbd+yAJCQY2fTxVCqF8fExmDKzF6h86ZAABhcKisGFZVRVxZGjx1bM971zh40dqYwJCZKq8kBLZaWnZw8sKxPgBYBQKIREIs7GjlS2LEPj2DMqK263G7t7ehBZ1gPn5s1bMFkaQWVMqE42Ny8wBhcesm8fGztS5TCEjFSSjRypvNTW1qBrW1eu3hfIHGrZ2JHKlSILeNn3hsrMgQMHc9m8ABAMLiASjQLMXqAyZMoqUkn2vSk0Bhceslpjx342dqQyZSls5Ejl6ejRI0gsOwQMDw9DgNW+VH4kmIjH46zzpbLTuW0bfD5frgcOANy8cQMaWC5M5ceQFDhdLruXUfH4xLyKhxs7jrOxI5UjWUE6zUaOVJ62b++CQ3XkUskNw8Dt27cBi6nlVGYsAx6Px+5VEG2YLMvoO3FyRWnE6OgoLAieiam8yCpSyRRkmYGxQuPOsIoHjR01LZOCy8aOVI7SpoDCRo5UplRVxYGD+xFa1gPn9u3bkBksozIiCUDXdNb4Utna09sLSVpq7GhZFm7fvs2xlFRW0paAycbQRcHgwioyjR2PYnExlPvYwMAAGztS+WAjR6oA+/ftg2EYuR44qVQKo6OjkCzD5pURrY+ppwFYdi+DaNM8Hg8OHDyIxVAw97GBgTscS0nlQ5JhWIDfX2P3SqoCgwtr2Ldv/4rGjpFIBKEQGztSeWAjR6oEzc3NaGxsQDy+NGv9xo0bkAQf1qj0CQCKLLEkgsreocNHoOtLgd5kMomJ+xMcS0llIW1JiMdiLBMuEgYX1hCor0dHR+dDjR37oVn8xqTSZ8ls5EjlTwiBUydPIRqL5T4WDocxP78AmVsxlTrLWBEYIypXjY2NaGtvX3EmvnXzJsdSUukTApKioi4QsHslVYPBhcc4fvyplY0dx8ZgsbEjlTpZZSNHqhi7du2Ex+1BKrWUiXP9+jVYJsdSUmmThMXxk1QRhBA4ceLkijPx/Pw8YrE4x1JSSdOFgtBiiI0ci4hPyY/Rtf3Rxo43bt5gExsqaWnIkNk8jCqEoig4efIEFheXupVPTU0jlUxCYvyMSpQkwM7kVFG279gBj9eL1LKxlDdu3uCodiptispeC0XGHeExVm3seOcOLElm9gKVpuz4SafTafdKiPJm3769kGUpN5YSAK5duw7LYPYClSZTT0OWeU6gyiHLMvr6TiC8fCzlyAgswTMxlSZTVhEOh3kmLjLuBk/wcGNHXdfRf6uf2QtUktKWjLSWtnsZRHnldrtx5MiRTFPdrJGRESAzbZ2opIjs/9xut91LIcqr3r17IYTIjaU0TRMDd27D4JmYSpAOGarKqWnFxuDCEzxo7Bhd3tjxdj8gKQBr2qmUSAqSqRQCgXq7V0KUd4cPH4JpWjDNzJxq0zRx61Y/YOlP+C+Jissy0mzkSBXJ6/Vi//79WFwW6L1z5w4nqVHpkRWk0yn4/X67V1J1GFxYh+PHn0JiWRMbLZ3GwMAAdMHNlEpHGhJCoSAbOVJFCgQC2L17FxYXF3MfG7hzh1MjqKQIAJZloq6u1u6lEBXE4aNHoet6LqM3kUhgcnISJgMMVELSlgRN4+WDHRhcWIcd3d3w+/0rAgw3b94AFBVgUi6VAklGWtPR0tpm90qICuapp44jnU7nDrXpdBrDw8OQYNq8MqIMy0hjYX6BQV6qWE1NzWhtbUU0Gs197ObNGxxLSaVDSLCExPGTNmFwYR1kWcaZZ55BZFkTm1QqhcHBezA4godKQBoyZufm2LSGKlpbWxtaWlsQi8VyH7t58xaDC1QSBADLNNDQwNI0qlxCCPSdOIlEfGkfnpubw0IwyOwFKgmakBEOhxnktQmDC+vU07MHHq8HyeUjeK7fgCU7wOwFspUkQzdNtLUxa4EqmxACp0+dQmxZPXskEsHs7BwkYdm4MqJM1sLo2BhcLpfdSyEqqB3d3XC7PUinU7mPXbp4CabE4ALZTUAoKgLMWrANgwvrpKoqzpx5GuFl9b6JRByjIyMwmb1ANkpDwvTUNA+0VBV27NgBn9e3ItB7/fo1wGRtJdnnQdZCa0ur3UshKjhFUfBUXx8WQ0tn4oWFeczOzTJ7gWylSwqCwSAUhc9mdmFwYQN69+6Dy+VaEam9dv0aTJljTsgmQoIJCS2tLXavhKgoZFnGqVMrZ63PzMwiEY9DYhIZ2cQy0hgZHUVtbY3dSyEqir379gNAbiwlAFy+dInBBbKPEICswufz2b2SqsbgwgY4HA6cOn16RaQ2Fo3i/sQEN1OyhSZkTN6fgMfjtXspREXT29sLRVGhaVruY5cvXwZM7TH/FVFhPMhaaGtl1gJVD5/Ph30PjaUMhUKYmpzimZhsoQsFk5OTcLs9di+lqjG4sEH79x+Aqq481F69eoUbKRWfkGAJGU1NzXavhKioXC4Xjh47itCyQO/ExH1EIxFIYO8FKi7LSGN0dBS1tRw/SdXlqb4T0HUdprnUVPeDDy4zo5eKT0iwJAVeZi3YjsGFDXK6XOg7eQKhYDD3sXA4jOnpaQYYqKg0IWNiYgI+v9/upRAV3eFDh2BZ1opD7YULFyAs4zH/FVF+ZbIWTLQya4GqUENDAw4cOIhgcCH3sXA4jInxcQYYqKg0IePuvbuor+e0HrsxuLAJBw8ehiTL0PWlBmJXr1xhl1wqHiEASUE9R55RlaqtrUFvby9Cy5rszs7OYW5ujqMpqWgyWQsjzFqgqtV38iRMw1jRe+GDKx9kL9zYCIeKQEgwhQy/j5dtpYDBhU3weDx46qmnEFxYitQGg0HMz88ze4GKQhMKxsfHUVtbZ/dSiGxz/PhRaGkNlrVUCnHp0kUGF6goHmQttLSwoS5Vr0AggMNHjiK4LKM3Fo1idGQEBi/dqAg0oeDWzRvo6Oy0eykEBhc27fCRoxBCrMheuHLlA5gSR59QgWW74XKGL1W7lpYWbN++fUXvhVBoERMT9xlgoILLTIgYQV0dg7xU3Z7qOwFY5orshatXr8BSmL1ABSbJ0C0Lzc0tEILfa6WAwYVN8vl8OHL0KEKhpUjt3NwcFoJBZi9QQWWyFsZQx+ACVTkhBJ599hmk0qkVvRcuX77M4AIVlAAAy0QrsxaIUFNTg6PHVmb0xuNxDA3egyHz0o0KJw0Zt271o6293e6lUBaDC1tw7PhTsExrRaT2/LlzrDOjwpFkmJDg93OWOhEANDc3Y+/evQguG4cWi8UwODgEYemP+S+JNs8yNAwPM2uB6IHjTz0FPJTRe+3aNViymsm4JMo3SUZa09HZ2cGshRLC4MIW1NTU4OChQysmRywuLmJ4eBgGsxeoANJQ0H/rFhobG+1eClHJOHPmNIyHGopdvXoVsmCYl/Ivk7VgoKWFY4CJHvD5fOjr61vReyGZTOLuwAB0lgxTAaSFgoGBO2huZgZZKWFwYYuOP9UHwzBWpORe+SDbe0Hwn5fySFYRi8fR0tZm90qISkp9IIAjhw+vONSmUinc6u8HTGYvUJ4ZaQwODrHvDdFDjh47BlmSoGla7mPXr18HJGYvUJ7JCuLxBLq277B7JfQQPv1uUSAQwN59+1dkL6RSKVy9egUau+RSHmlCwdVrV9mZnGgVJ06egAWsSMm9eeMmBExmL1DeSAKIx2Noa2u1eylEJcfj8eLkqVMrzsTpdBr9/f3QeSamPEpDwdDwEBoaGuxeCj2EwYU8OHHiBHRdX5GSe+f2baQ1HWAjG8oDQ1YxNjaGnt09rCsjWoXf58PJEyewsOxQq+v6/9/efXdFdbbtH//uvafQO1jQRFGDBXvvsceSxOR+fu/neUFP2p3kTqyJBQsqdmMBRREUGGaGOmW33x+j3sEWddShHJ+VLNfaM+C5EDenx76u8+Lq1asYnv2ajxR5C57N7TstWrUg8gqLFi8hGAySTqefXfvrrxv4pqUVvfJeeFaQnp4e6urqcl2KvIT+lr8HlVVVLF6yZMSUXN/3aTrXhGMoqZUsGQa+GaSt7Z6m4Yq8xtKlSwgGRja1t2/fwbZtTGVykiXTd7nfdp85c2bnuhSRUSsvL49Va9bQ97chu7Ztc+niJa3olffAwDWDdHZ2UlqqgbqjkcKF92TV6jVYljWiqX3U2UlvLKqjKSUrjhnk8uVLLFu+QqsWRF4jPz+fdevWjjg5wvM8zpw5g6HZC5IFAzDw6OjspEKrFkRea+HCRYTDYVKp1LNrLS13GE4k1RNLVhwryPVr15g3f36uS5FXULjwnhQWFrJ+w0bi0diI65mjKUNoZrm8E9PC8TLLu3Xkmcg/a2hYQEF+Aclk8tm1x48f093djeG7r/lIkdfwbM6dO8/iRQtzXYnIqBcOh1m7bt2I1Qu+73Pq1Ck8U8e1yzsyLVzfwLbTFBUV5boaeQWFC+9Rw8KFlJaXMTQ0+Oxaf38/d++24iiplXdgGwFOnz7NkiVLc12KyJgQCoXYtGkDfX19I643NTVhGb5aWnlrpgG2nVmVqFkLIm9m3vwFFBSMDHpjsSj37t3VcEd5J7YR4MTJ4zQsXJTrUuQ1FC68R4FAgC1btzI4MIDv+8+uX758Gd/QIBt5O74VoH9gkClTJhPOy8t1OSJjRn19PWVlZQwNDT27Njw8zPXrN8DXcEd5S57NiRMnWLZsWa4rERkzQqEQa9evH7F6AeDixUu4hgGmlaPKZCzyrSB9/f3UVE8iPz8/1+XIa+hfu+/Zp5/OYMbMOuLx/26PsNNpLl26qEE28lYcM8iFC+eZ81l9rksRGVMsy2Lz55sZGBwZ9N64cQNXwx3lLZi+y+NHj5g5cyZ5eeFclyMypsybN5+KigoGBweeXXMcm6amJvXE8lZcM8DZM2dZ0NCQ61LkHyhceM8Mw2DTps3YaXvE0ZQtLS0MDQ/jmTqaUv6ZY4W4fesWDQsXYVlK90XeVt3MmdTNrCP2t6MpM8Mdz2q4o7yRp0McL1++zGdz5uS6HJExJxAIsH3nToaGhvA879n19gcPiMXiT+YviLyeYwW5dfs2i5csUU88Bihc+AAqq6pYtnw50eeOpmxsbMQLhEAT/+V1TAvbg87OTqbq6EmRd2IYBps/34zjujjOf8OER48e0dPTjanhjvJPPJuzTU2sXr0a01S7JPIuamun0dCwkGhv74jrZ86cxgsE1RPL65kWjm/wsL2d2mnTcl2NvAH9tPxAVqxcRTAQGHEMT19fHzf/+gvHDOWwMhntbDPE4UOHWL16Ta5LERnTKsrLWbN6Nb1/C3oBTp8+g4Gn4Y7ySiY+ycQw6VSampqaXJcjMqatW7+BwHM98eDgIDdu3ND2CHkt2wxy5NBh1q5dp+PYxwiFCx9IQUEBGzdtIh4beTTltWvXSKZt0OkR8hKuGaS9vZ2amhpKSktzXY7ImLd8+TKKCosYHk48u5ZMJjl37jyGhjvKKxi4HDhwkNWrV+W6FJExr7CwkM1bthCPxUbOwbl+nbTjgqUtw/IizwrS2dlJzST1xGOJwoUPaP6CBioqKhgY+O8gG8/zOHWq8ckxPErg5G8ME88M0Nh4giVLdfSkyPsQCoXYtm0L/f39I5rae/fuEY1GMbQ9Qp5j+DYXmy8yd+5cCgsLc12OyLgwb958ptbWjjgm2PM8zpw+raMp5UWGiWsEaGw8qZ54jFG48AFZlsWOnbsYfm6QTSQS0Tm/8gLbCnHkyGHWrd9AOKyp5CLvS11dHTNnziD+3JFopxpPYWp7hPyNiU9yeJjWu3dZsGB+rssRGTdM02Trtu2kU6kRA8+7urp48KAdx9KWYfmvpz3x6jVrCQb1vTGWKFz4wKbW1rJk6VJ6I5ER1y9evIjjAzo9QgDXCtITieC6LnV1s3Jdjsi4YhgGn3++GdtxRgx3TCQSXLjQrO0R8oyBy88//8K2rVs0lVzkPauurmbFylVEe0f2xOfPn8N2fW2PECCzRbiruxvXcdQTj0EKFz6CtevWk19QwPDw8LNrjuNw8uTJJ0mtnptNaIaJZwQ4fPAAmz/fooE1Ih9ARUUFG9avJ9I7crhja2sr8Vhcp0cIpudwsfki06dP1xBHkQ9k5apVFBQUkniuJz5x4viTgefqgSY008IzAxw5dIhN6onHJIULH0FeXh47duykv69vxPaI7u4uWlpatBRsgnOsMAcPHWDFytUUFRXluhyRcWvp0iVMqqkesecXoLGxUadHTHAmPsOJIa5eu8aaNatzXY7IuBUOh9m2fQd9z83BiUQi3Lp9Sz3xBOdYIX7//TeWr1hJcXFxrsuRd6Bw4SOZMXMm8+bPJ/rckWiXLl0kkUrj6fSICcm1Qjxof0AqkWTuvHm5LkdkXAsEAuzatZNkKjVie8Tw8DBnzzZh+s5rPlrGKwMwcfn3v39m184dmnkj8oHNrKtj9uzZxJ7ria9cvsxwMoWnLcMTkmOFaL3bSjKZZP6CBbkuR96RwoWPxDAMNm7aTMCySCWTz657nsfx48fwzCAY+uOYUKwAaQ8OHjzElm3bMU39+Yt8aNXV1axbu5be57ZH3L9/n/aH7RgKGCYcw3c4ebKRT6ZPZ9q0abkuR2TcMwyDz7dsxTAMUqnUs+u+73P8+HE8K6SeeILxzQAp2+XIoSNs37FTPfEYpj+5j6ioqIit27YRe+6c376+Ppqbm7G1FGziMAwcM8RPP/7A6tWrKS8vz3VFIhPGihXLqaqupK+/f8T1prNN2KkUJt4rPlLGG8N3ePzoES2traxduybX5YhMGCUlJWzbsYNYNDqiJ+7v7+Py5cvqiScSw8ANhPjxh+9Yt369euIxTuHCR1Y/dx5z5nxGNNo74npLyx16eiK42h4xIdhmiObmC5iGwaLFi3NdjsiEEggE+GLXLpLJ5IjtEa7rcuzYnzqecoIwDfAcm3//+2d2f7FL2yFEPrL6+rnMnTf/hdMjbt26SSTSq554grCtME1nzxIKhVm4aFGuy5EsKVz4yAzDYOv27QQDQRKJxIjXTp1qxPYMfO01G9dcM0isr4+mpiZ2frFbx52J5EBNTQ1rVq8m0ts74qlZPN5Hc/NFHU85zhmA6Tv8+ONPLFzUQG1tba5LEplwMtsjthAK5Y04UQ3gZONJ0p6h4ynHOdcKEo3GuNjczM4vvlBPPA4oXMiBwsJCdn2xm/6++IjTI9LpNH/88Qeu9pqNX1YAG4Pv/u//2Lp1G2VlZbmuSGTCWrVqJVOmTCH+3OkRd+7coae7W8dTjmOGb3Pu3HkSySRr12g7hEiuFBQU8MXu3Qz094/oie10mmN//pk5nlI98fhkBbB9k++//44dO3dRWqqeeDzQ39YcmTFzJkuWLqM3MnIpWCwWpelcE05AyzPHHcPEMUP8+P0PfPrJJ8ybPz/XFYlMaIFAgD27v8D3PJJ/GyoG0Nh4CsfW/IXxyPBdeiMRzpw9y769ewiFtLdbJJc+nTGDpcuW0RvpGXE9Gu3l4sWLmr8wHj3piX/4/ntmzZrNnM8+y3VF8p4oXMgRwzBYv2Ej5eUVL5y53nbvHvfa2nAsBQzjiWOFaTzVyODgAFu2bccwtKtbJNfKysrYtWsnsWhs5FMz2+bo0T8wfM1fGE8MPJx0iu++/4GtW7dQU1OT65JEBFi3fgOlpWUMPDdo986d23R0dOIoYBhXnECY4yeOk0wMs3nzZvXE44jChRwKhULs2bcXO50inU6PeO38uXP0DQ5qmM044Vgh7rW10Xz+Anv27iM/Pz/XJYnIE3PmzGHJksVEekcO2u3r6+P06VOY6HjK8SAzZ8Hl/777jk8//ZSFDQ25LklEnsj0xPtIpZIv9MRnz55hKJnKHNsuY55jhWltvcvVy5fYvXcf4by8XJck75HChRyrqqpmy9ZtRHt7Rzw1830/s9fMNzXMZoxzzSD9Q8P8+uvPrN+wnqkaHCYyqhiGwaZNGykvK39hJVl7+0Nu3byJqQGPY5oBWDgcPHiQdDrN9m1bdY66yChTUzOJLdu2E42O7Ild1+WPo0exDfXEY51rBukbGOT3335lw8bNTJ48OdclyXumn6yjQMPCRTQsXPjC/IVkMsmff/6hYTZjmG8GcDD5/rvvmDmzjuUrVua6JBF5iVAoxL59e0in7Reeml2+fIXuri4MXysYxirTd7hwoZnbt1vYt2+vVo+JjFINDQuZP7+B3sjIlWTDw8McPXo00xObOlFgLPLNzFDz77/7P2bMrGPJ0qW5Lkk+AP2LdRTIHMWzlarqauKx2IjXent7OX36FE4gD7QfaWwxLRwrxE8//YRlmuzcpSN2REazqqoqtm/fRm9vdMRTM4CTJxtJDg/pBIkxyPQdHjy4z4mTJ9n8+Sam6EmZyKhlGAZbtm6lvLyc/udWksWiURobT2ZmkqknHlue9MQ///RvAoGAeuJxTOHCKBEKhdj35ZcYhkHiubN+29vbuXT5Eo6VBxotNjYYJk4gzJFDB+nqesSXX3+tJ2UiY8CCBfNZumwJ3T0RfN9/dt11XY4cOYrr2Bg6QWLMMH2X/r4+fv7lP8ytn8uSxYtzXZKI/INwOMy+r77CcRySyeSI1zo6Ov7WE8uYYJg4VpjDhw7yuOsRX329Xz3xOKZwYRQpLS1j35df0d/fj+OMXH57+9YtWlpbsHVE5ehnGDiBPE6fOs2NGzfY9cVuqqqqc12ViLwBwzDYtHEj02priT63kiyRSHDo0CEMz8FUzjvqGb5LKjnM9z/8SHVVJTt3btecBZExoqKigt179xKPxXHdkSvGbt+6xd22ezpVbSx40hOfOn2Kv27cYM+efVRWVeW6KvmA9FN2lJn+ySds/vxzIj09I56aATQ3N/Po0WPdTEc5x8rj6tWrnG9qYvXqNXz2WX2uSxKRtxAMBtm7dzfhcJiBgYERrw0MDHDkyBEMz1bAMIqZvodrp/jhhx9xXYcvv9xHKKSj7ETGklmzZrN+wwYiPd0vbFW7cP48PdGojqgc1QwcK4/Lly9x/lwTa9etY9bs2bkuSj4whQuj0JKly5g3fz6R7u4XAoZTpxqJ9ffrZjpKOYEwd9vuceL4MT6dOYM169bluiQReQdFRUV8s/9rkqkUyVRqxGvRaIw//zyG4TvaqDYKmXh4bppffvmVaDTG/v1fU1JSkuuyROQdrFy1igULGl546Ob7PsePHSPWP6CeeJRyAmFaWltoPHmSWbNms2r1mlyXJB+BwoVRyDRNtm3fwZSpU4k+d+6653n8cfQPBoeTuLqZjiqOFabzUReHDxygvKKc3Xv2aliNyBhWU1PD3j17iMdiL2xV6+7u5lTjKSwUMIwmpgF4DgcOHOBBeztf7N6lAY4iY5hpmmzZtp1p06e90BO7rsvRI0foGxxSwDDK2FaYjs5HHD1ymLLycg1wnEAULoxSoVCIfV9lnrbE4/ERrzmOzaFDB+kfTihgGCUcK0zH48f89tt/CIXDfL3/Ww2rERkH5syZzaZNm+iJRF7Y9/vw4UPOnb+AqRUMo4JpgOHZHDp0mJaWu6xdu4a59dqWJjLWBYNB9uz9kuKSYvqe64ld1+XI4cMMDKknHi1sK0zn48f8/vtvhEJh9n+jnngiUbgwihUUFLD/22+xTOuFfb+2bXPo4CEFDKOAbYXpePSYw4cO4dg2+7/9VktwRcaRFSuWs3LlCrp7Ii/s+73b2sqFCxcwtYIhpzLBgsMff/zJzVu3mD9/HmtWr851WSLynhQUFPD1/m8xDIOhocERrzmOw+HDhxhMpHCtYI4qFHjysK3zEYcOHsR1bL759l/qiScYhQujXGlpGd/+61+k02kSicSI1xznScCgtDZnMsHCI/744yiDAwPs//ZbnQwhMs4YhsHGDRtY2LCA7u4Xh+22trbSdPastkjkiIkPns2RI4e5dv0Gs2bVsWPHdi3BFRlnysvL+fqbb0gMJ144otK2M6t6h1K2AoYcsQNh2js6+eOGnxiWAAAY3ElEQVToEYaHhtj/zb90MsQEpHBhDKiuqeGrr/fT399POj1ysFhmi8Qh+oYS2m/2kT3dT3b82DGi0V52791Lbe20XJclIh+AaZps27aV2bNn0ROJvBAwtLXdp1EzGD46Aw/fzQTtN2/dZvq0Wvbu2UMgEMh1aSLyAUyZMpUvv/6a/r4+Us8N202n0xw8cICB4ZR64o/MDuTxoP0hx48fIx6Ps/fLL5laW5vrsiQHrP/93//931wXIf+srKyM8vJyrl65TCgUHvFExvM82truMXlqLeH8Qkzffc1nkqwZxrOb6MmTJ4j09LBt+3YWLGjIdWUi8gGZpkld3Uw6Ojrp7u6msKBgxOv9/f1Eo1FmfDodwzDxX/F55P0w8PCdNAcPHuReWxtVVZXs3/814bCOaxYZz8rLy6mqqubKlUsEg8ERYaLruty9e5eayVPIKyhST/yhGQZOII/79x9wqrGR3kiEHTt3Mnfe/FxXJjmicGEMqaqqpqy8nGtXrhAKBbGs/95MPc+j7d49SsvKKCotx/R0M/0gDBMnkM/1G9c519REbyTC1m3bWbJ0aa4rE5GPwLIsZtXV0XavjWg0SsFzAcPg4CA9PT3MfBYwaB3Dh2Di4aSSHDhwgIcdHRQVFfE///qXhoaJTBAVlZVUVlQ+eegWGvHQzfd92truUVperp74Q3raE/9141lPvGXrNhYtXoJh6GffRKVwYYyprq6mrLyMa1euvhAw+L5Pe3s7VjBIRc1kTN8DPTt7f8wATiDMmbNn+OvGDQULIhNUMBhk9uxZtN2/T+9LAoahoSE6OjqY8eknWKaBb2gH4vtk+A6JoQEOHTpER+cj8vPC/L//+RdFRUW5Lk1EPqLKqirKysq4dvUy4XDeC3NW2tvbCYXzKK+u0QqG980M4ARH9sTbtm9nydJlChYmOIULY1B1dTXlFeV/S2tH7i3t6uoikUgwefqnmYDBV8CQLc8M4JhB/vzzDx7cv09vpIdt23coWBCZoEKhEHNmz6a9/SE9Pd0U5BeMaKiSyRR3796ltnYK4VBQAcN7YvoOjzs7+fPPP3nc1UVJcTH/7//9j6aRi0xQ1dXVFBeXcO3qFcJ5LwYMjx8/wnVdqqdMw0Q98fvgmQFsM8AfR4/y4MGDZ1shFi1ekuvSZBQw/OenUsmYcfPmX/z26y+UlVe8dI/p5MmT2bhpM5ZrY3p2DiocH1wzRNr3OXL4ML29vc+ChcVLFCyITHTJZIqff/6Z9ocd1FRXvfDExjRN1q5by9SptXiGhgy+KwMwcbh29RrXr1+nN9pLZWUV3+z/msLCwlyXJyI5du3qVQ4dPEBZWRnhvLwXXp8yZQobNmzE8mxMz8lBheODa4VIOh5HDh8iGo0Sjfayc+cXNCxcmOvSZJRQuDDG3b59i99+/YXCouIXluYCFBcXs/nzzykIhwi46RxUOIYZBrYVJtIbpfHkCfr7++mLx9i2fSeLFi/OdXUiMkqk02l++fVX2u61UVNT89IloQsWzGdBQwMeAW1We0sGHqbvcvJkIx0dHfREIkydOpWvv/qSvJf8I0JEJqa7ra388vNPFBQWvbQnLiwsZMuWrRTkqSd+a0964mg0xokTxxno7ycej7Pziy800FxGULgwDjx8+JCffvgeKxB46dJQy7JYuXIVn0yfTsBNge/loMoxxgzgWCGuXrvKXzduMDg4SDKRYN+XX1E3a1auqxORUca2bX777XfutLRQU12Nab64DWLq1KmsX78OzACeToJ+I4bv4KRTHD36B319fXR39zBj5gz27d1DKKSj5kRkpM6ODn74/rvX9sSrV69hWm2teuI3ZQVwzBDXrl3jxo3rT3riYfbs/ZLZc+bkujoZZRQujBO9kQg//PAdyWSKioqKl75nxowZrFq1GtNNa0nYa7hmEBuT48ePEenpoS8exzAM9n/zLZOnTMl1eSIySrmuy7Fjx2m+eJGqykqCweAL78nLy2Pjxg2UlZfjG0GtYngFg8x8hQcPHnD+/HmSySQ9kQjz5s1l544dL/3aiogARCI9fP/dd7i2TWl5+UvfM3v2bJYtX47p2piutg6/imsFsT0j0xNHIsTjcUzTYP9+9cTycgoXxpHBgQH+/e8f6enuoaq6+qVLc0tKSvj88y3khQIEPFuDbf7OMLGtELFYjBMnTpBMJon29lJcUsz+b/5FWVlZrisUkVHO932uXLnC4SNHKS0peeXRiPPmzWPRooV4WHg6rnIEw3cxfJdTp07T0dFBMpUiFouxccMGVq5c8dJVISIif9ff18ePP3xPPB6nsurFeTgAZWVlbNiwkYK8MAEvrZ747570xJFIhJONjaRTKXojEcrKyvj6m28oLVVPLC+ncGGcSaVS/P7bf2htaaG6puaFqbmQGTC2cOEi6ufWYzpaxQCZ1QqeFeDC+QvcvduK53n09HQzrXY6e7/88qV790REXuX+/fv8++dfCFjWK08yKC8vY9OmzQRDYXxTwx4NwPBtor29NDaeIplM0j8wQDqVZs+e3cyZMzvXJYrIGJJIJDh44HfutrZQWVVNIPDifdYwDBoaFjJv/jytYnjCtYJ4ZpCLzc20tNzJ9MTd3Xz66Qx27937ytBcBBQujEuu69J09gxnTp+mpLT0lTeB0rIy1q9bT2FBPkHPnpj7zkwLxwzR1d3N2bNnSSYTpJJJYrEYS5ctY8PGTVp+KyLvJBqN8uNP/2ZgYIDKioqXPjmzLIuFCxuor6/Hw5ywsxgM38XE4+LFS9y5cwff94nGYuTn57P/66+orq7OdYkiMga5rsuF8+doPHnytT2xVjGQ6YmtEI+7umg62zSiJ16ydCmbNn/+0oBG5O8ULoxjbffu8dt/fsHzfMrKy1/a2BqGwWf19SxetBjDs7EmSmJrGDhmEBeDs2fO8PDhQwD64nEc12XXF18wZ85nL/2aiYi8qeHhYQ4ePERr610qKyteGVYWFxezZs1qysrLwQziTZCfzKYBhufw6FEn585lZis4jkOkN8on06exZ89uHTUpIllru3eP//z6C0DmPvsSmVUMDcybPx/DcbC8iXKihIFjBXE8OHPmNJ2dnQDE43E812Xnri+Y85l6YnkzChfGuf7+fn77z690dnRQVV390m0SAAWFhSxftpwpU6eM+2VhrhnCDwRpbWnhypXL2LaN53lEIj1UVVaxd9+XlL9iKKaIyNvyPI8rV67y57FjhEIhSl+xTQJg+vRprFq1CsMKgDF+j600AMOzSSQTNJ1toru7G4DBwUGGhodZt3YtK1Ys11MyEXlv4vE4v/7yM93d3VRVVb2yJ87Pz2fp0qVMmz59AvTEQfxAkJaWFi5fuoTruriuS28kQs2kGnbv3queWN6KwoUJwHEczpw+xbmmJoqKiygsLHrle8vKyli+fAWVlRVYno3hjp95DJ4VxLOCtD94wKVLl0kkhoHMnry+eJxFi5ewafNmHW8mIh9ET08P//nPb0SjUaqqql45mNCyLBY0LGBu/dzMCgZz/IQMBsCTbXjNzRe5d+8evu9nAt7eXkqKi9mzZzdTNIVcRD4A205z5vRpzp87R2FRIUVFxa98b1lZGStXrqK8rIyAb8N464nNIJ2dnVy82MzQ0BAAyUSCeDzOsuUrWL9hg7YGy1tTuDCBtD94wMGDBxgY6Key8tWJLUB1dTXLV6ykuKiQoO/CGE5tn95Au7q6aG5uZmCgP3Pd8+jt7SU/L49tO3ZQVzdLS75E5IOybZuTJxtpbr5IcXHRa5f8B4NB5s6tZ968eXi+MaZDBtMA37XxXIcrV65y9+5dPC8z5yeRSBLvi7N48SI2bthIXl44x9WKyHjX2dHBgd9/o6+/7x974ilTprBs+XIK8guwfGcMr2Qw8KwAnhWku6uLS5cuEY/HgSc9cSRCOC/Mjp271BPLO1O4MMGk02mazp7l/Lkm8vLzXznF/KnJk6fQsLCBiooKTNfBHCvHVxomjhHACATp6Ojg+vVrxGKxZy8PDg4yNDjI4iVLWLtuvSbfishH1dZ2n0OHDz8b9vi65f+BQIDP6j9jwfwF+IBhjZ2ZDKYBuDbpdIrLly9z//4DnrYdrusSjUYJhcLs2rWDuro6NbMi8tGk02nOnnm6iqGIoqJXr+yFzIO3hoYGqmsmYbg21ljpiU0LBwsjEKSzs4MrV6/S9yRUABgYGGB4aEg9sbwXChcmqK6uLg4fPEBPdw9lFeX/uBWgpKSUufPmMmPGDHzXIYg3CpeHGWAFsDHxMLhz+za3b98mmUw8e4fjOESjvZSWlrFz1y5qa6flsF4Rmchs26a5+SKnz5zBsizKy8pe+49ry7L49NNPqK+vp6SkBM838A1r1K1myKxScAhYBj2RCDf/uklHR8ez133fp6+/n1QyxdKlS1izZrWaWRHJmc6ODg4e+J14PE5pWRnh8OtXTxUVFTFv3jxm1s3Cd2yCxmjsicG3gjhYOK7LzZs3uXu3lVQq9ex127aJRaOUl5ezY9cXTJ06NYfVynihcGECcxyHK5cvcfr0KRzbofwfnp7Bk+Z2xgxmz5pNeUUFnp0maPhPbqo5+FYyDHwziO2DFQjS3d3F7Tt36Ozo4O/f2q7rEotGMQyDVavXsGz5MoJBzVYQkdyLxWIcO36clpZWSoqL3+h0hKKiImbNnsWc2bPBMDDMAD5mzoIG0wA8F8PwSQwPc/v2He7fv08ymRzxvuHhBP39/dTWTmXLls+ZNGlSbgoWEfkbx3G4cf06jSdPkE7blFeU/2NPHAwGmT59OrPnzKG8rBwv10GDYeKbgUxPHAzR1fWYv/76i67Hj0e8zfM8YtEovg/r1q9j8ZKlmq0g743CBWF4eJhLF5u5cP48Pj7l5RWv3Xv2VDAUonZqLTNmzmBSzSRcxyZggIkHnvthlooZJpgWLgYeBpgWHQ8fcv9+G48fP8Z13RFvf3oD9TyPxUuWsmLFCoqKXz28R0QkF3zf5+69exz78xixeB/FRYVvFDIYhsGkSTVMnz6dadOmEwwF8Twf88nWiQ/1A94ADDw81yEYsBgYHOThw4e03Wujr6/vhfcnEgn6BwYoKipiy+efM2tW3SsHWoqI5EoikeBi8wXOn2vCME3Kyyve6F6Vl5fHtGnTmTlzJhWVlbiOjYWPhQeuywe5G/+9JzYy4XLHww4ePHjA48ePXtoTx+MxXMdhQcMiVq1e/Y/bo0XelsIFeWZgYIDz55q4cvkypmlSVl7+RiEDZFY01EyaRFVVFZNqJlFeUUHmQZZNwDQwAXwvEzg8/fVVDCNzw3zyq+eD44MVDOLYDr29vXR1dxHp6SESifCyb+HMDTSOY9vMX7CAVavXUFZW9k5fFxGRj8V1Xe7evUtj4yl6o1GKCjMhw5vOIigqKmLSpEnU1tZSXV1FKBTCdhx8DCzTwjfMZ7fff/rh//R3NA3w/UyQYBqZGRBDQ8N0dnbw6NEjurt7sO2XDzgbGhpicHCI4pJi1q1dy2efzdETMhEZ9fr64pw+dZpbN29gGJme+E2PxrUsi8rKKqqrq5kyZQoVFRX4vo/vOlimgWWQ6YU9L/Pr6zzrhzM9seuD+2RlgmPbxOIxuru66ejsIBaNvvRTeJ5HPBbDcRzq6+eyas0aKisr3/IrIvJmFC7IC2LRKM3NF7h+7Rq+71NSWvqP+89eprCwkIrKSkpLSikqKqSwsIiCggLCeeEnWxJe/NbzfbDTaZLJJMPDwwwODTI0OEQ8Hqe3NzJir9jLpNPpzFMz36d+7jyWr1hBdXX1W9cuIpJLruvSdv8+jY2NRHoihMNhSkpK3vppv2VZlJaWUFpaSllZGRWVlRTk5xMIBAkEAgQCmQDZ83xM08AwDDzPe3bWeTpt09ffRywapb+/n/7+AQYGBl54IvZ3vu9nBoQlElRWVrJ+3Vrq6ureOKwWERktYrEYV69c4fLli7iuS2lJKeG8vLf+PCUlpZSWlVJYWEhJSQklxSUUFhaSl5eHYZqYppkJIHw/0wwbBr7vY6fTpFIpkskEiUSCWCxONBYlFo2STqdf+3umkkn6+zMnpNXPncvKlauorKp6p6+DyJtSuCCvNDQ0xF83rtPcfIHhoWHC4TDF79DcvsyrnsK9y7ej53kMDg6STAwTzstj6dJlLGhYSLG2P4jIGOd5Hg8etHPlyhVaW+/iA8VFReTn5723kxVM0yQYDOK6Lo7z7nuFE4kkA4MD4ENt7VRWrVrJJ598ou0PIjLmJRIJbv71F+fONTE8NPRee+KnDCMT8D4NGl4X4r6K53n09/eTTqUoKipi6bLl1NfXa0uwfDQKF+Qfua5Le/sDLl+6RFtbG/gewWCIouLiN14i9iFqGhwYIJVOYQDTpk9nydJlfPLJp1pyKyLj0uDgIK2trTQ3XyIWj2GZJkXFxYRDoZwd4ZhOp+kfGMDzMk/0Fi9ezOzZsykt1T5eERl/HMfhwf37XL9+jXt3W/E8n3BeHsXFxTkLUp/viWfMrGPp0mXUTpumFWPy0SlckLeSSiZ52PGQ27du0draguM4mIZJfkEB+fn5H+zG6nkeyWSSxPAwrudimRYz6+qonzuX2tppFBQUfJDfV0RktPF9n66uLu60tHDr5m0GBgbwgXA4RFFh4QcNfW3bZmhoiPSTGQuFBYXU13/G3Ln11NTU5CzkEBH52BKJBA/u3+fmzb+439aG7/sYQF5BAQUFBR+0J06lUgwPD+G5HpZlMmNmHZ99Vs/U2lqKioo+yO8r8iYULsg7s22bx48e0d7+gPb2drq7uvA8H/CwAgFCoRCBQJBgMIhpmm/UdLqui2Pb2I5DOp3GcWwMw8QAqmuqmTZtOtM/+YSpU2sJhXSUpIhMbL7vE4/HefToEXfvtXG/rY20bWcG6voQCgYIh8OEw+G3eoLlui6pVIpUKoVtZ+7DAKFwiJkzZ1A3s47JkydRUlKiQEFEJrxUMklXdxePHz/i/r37PH78CM/38D0/0xMHgwRDIYLB4Bvfiz3Pw3FsbNshmUjgeR6GAT4GFRUVzJgxg5kz65g0ebJW7cqooXBB3hvXdYnHYvT29vLoUSfRaJSB/n4GBgawbRvTzBxe9jzDyMyu8TyPQDBAcVExxcUllFeUM2XqVCorqyh/iym9IiIT1dMZNH19/cT74nQ97qKru4ve3iiO42T29GLw5D/gb6N1fcDIfI5QMERFZQU11dVUV1dRWlpGSWkJZaWlmqEgIvIPHMchGu0lEokQ7Y0Si/YSj8fp6+/DddwRoezTPvipzEzHzIO6woICioqLmDJlKpMnT6a8ooLS0jKFCTJqKVyQD873fRzHZnh4+JWnPYRCYfLz8wnlcO+wiMh49XQ4mG3bpNM2tm1j2+lMqBsIPPk/SDAYwLIs3YtFRD4A3/dJJpOZlQi+nznm1/PwPB/P8wgGg+Tl5ZGXFyYQCOo+LGOOwgURERERERERyYrWNoqIiIiIiIhIVhQuiIiIiIiIiEhWFC6IiIiIiIiISFYULoiIiIiIiIhIVhQuiIiIiIiIiEhWFC6IiIiIiIiISFYULoiIiIiIiIhIVhQuiIiIiIiIiEhWFC6IiIiIiIiISFYULoiIiIiIiIhIVhQuiIiIiIiIiEhWFC6IiIiIiIiISFYULoiIiIiIiIhIVhQuiIiIiIiIiEhWFC6IiIiIiIiISFYULoiIiIiIiIhIVhQuiIiIiIiIiEhWFC6IiIiIiIiISFYULoiIiIiIiIhIVhQuiIiIiIiIiEhWFC6IiIiIiIiISFYULoiIiIiIiIhIVhQuiIiIiIiIiEhWFC6IiIiIiIiISFYULoiIiIiIiIhIVhQuiIiIiIiIiEhWFC6IiIiIiIiISFYULoiIiIiIiIhIVhQuiIiIiIiIiEhWFC6IiIiIiIiISFYULoiIiIiIiIhIVhQuiIiIiIiIiEhWFC6IiIiIiIiISFYULoiIiIiIiIhIVhQuiIiIiIiIiEhWFC6IiIiIiIiISFYULoiIiIiIiIhIVhQuiIiIiIiIiEhWFC6IiIiIiIiISFYULoiIiIiIiIhIVhQuiIiIiIiIiEhWFC6IiIiIiIiISFYULoiIiIiIiIhIVhQuiIiIiIiIiEhWFC6IiIiIiIiISFYULoiIiIiIiIhIVhQuiIiIiIiIiEhWFC6IiIiIiIiISFYULoiIiIiIiIhIVhQuiIiIiIiIiEhWFC6IiIiIiIiISFYULoiIiIiIiIhIVhQuiIiIiIiIiEhWFC6IiIiIiIiISFYULoiIiIiIiIhIVhQuiIiIiIiIiEhWFC6IiIiIiIiISFYULoiIiIiIiIhIVhQuiIiIiIiIiEhWFC6IiIiIiIiISFYULoiIiIiIiIhIVhQuiIiIiIiIiEhWFC6IiIiIiIiISFYULoiIiIiIiIhIVhQuiIiIiIiIiEhWFC6IiIiIiIiISFYULoiIiIiIiIhIVhQuiIiIiIiIiEhWFC6IiIiIiIiISFYULoiIiIiIiIhIVhQuiIiIiIiIiEhW/j8qrbjLvnHDsAAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 1296x864 with 3 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "passmarks = 40 \n",
    "plt.rcParams['figure.figsize'] =(18,12)\n",
    "\n",
    "#creating a new column pass*** this will tell us whether the student are pass or fail\n",
    "data['pass_math']=np.where(data['math score']<passmarks,'Fail','Pass')\n",
    "data['pass_reading']=np.where(data['reading score']<passmarks,'Fail','Pass')\n",
    "data['pass_writing']=np.where(data['writing score']<passmarks,'Fail','Pass')\n",
    "\n",
    "#represent the ratio of pass and fail \n",
    "size = data['pass_math'].value_counts()\n",
    "colors = plt.cm.Reds(np.linspace(0,1,5))\n",
    "labels = \"pass\",\"fail\"\n",
    "explode = [0,0.2]\n",
    "plt.subplot(1,3,1)\n",
    "plt.pie(size,colors = colors, labels = labels, autopct = '%.2f%%', explode = explode, shadow = True)\n",
    "plt.title('Students Result for mth', fontsize = 20)\n",
    "plt.legend()\n",
    "\n",
    "#represent the ratio of pass and fail \n",
    "size = data['pass_reading'].value_counts()\n",
    "colors = plt.cm.Blues(np.linspace(0,1,3))\n",
    "labels = \"pass\",\"fail\"\n",
    "explode = [0,0.2]\n",
    "plt.subplot(1,3,2)\n",
    "plt.pie(size,colors = colors, labels = labels, autopct = '%.2f%%', explode = explode, shadow = True)\n",
    "plt.title('Students Result for reading', fontsize = 20)\n",
    "plt.legend()\n",
    "\n",
    "#represent the ratio of pass and fail \n",
    "size = data['pass_writing'].value_counts()\n",
    "colors = plt.cm.Reds(np.linspace(0,1,3))\n",
    "labels = \"pass\",\"fail\"\n",
    "explode = [0,0.2]\n",
    "plt.subplot(1,3,3)\n",
    "plt.pie(size,colors = colors, labels = labels, autopct = '%.2f%%', explode = explode, shadow = True)\n",
    "plt.title('Students Result for writing', fontsize = 20)\n",
    "plt.legend()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T21:17:44.064875Z",
     "iopub.status.busy": "2022-01-05T21:17:44.064561Z",
     "iopub.status.idle": "2022-01-05T21:17:44.888404Z",
     "shell.execute_reply": "2022-01-05T21:17:44.887340Z",
     "shell.execute_reply.started": "2022-01-05T21:17:44.064826Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5,1,'Correlation between the  attributes')"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA8UAAAOcCAYAAABnsxNTAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMi4zLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvIxREBQAAIABJREFUeJzs3Xd4VMX+x/HPZtMboROICIIbWkJHkOKlg4AYBFGRogIqBvVnA0EsqJeLAlcFC1eKiIqKBBGMoiIXKUERVFBAECO9hySkkHp+f+RmZd0kS3B3w7Lv1/PkITtn9pzvmUxIvpmZMybDMAwBAAAAAOCFfCo6AAAAAAAAKgpJMQAAAADAa5EUAwAAAAC8FkkxAAAAAMBrkRQDAAAAALwWSTEAAAAAwGuRFAO4bAwfPlzR0dEuv050dLSGDx/u8utcqEOHDik6OloTJ06s6FBwnkutn1yqJk6cqOjoaB06dMhaRp8GALgTSTHgpfbt26dnn31W/fv3V+vWrdWsWTN16tRJY8eO1dKlS5Wbm1vRIVaYbt26qVu3bhUdxiWHJM+Wt/QTR39s8uR2KCkhBwB4H9+KDgCA+82ZM0evvvqqCgsL1bJlS8XFxSk4OFinTp3Sd999pyeeeEJLlixRQkJCRYd6SUpMTFRQUFBFhwFcFh566CGNGTNGNWvWrOhQAABeiqQY8DJvvPGGZs+ercjISL388stq3ry5XZ21a9dqwYIFFRCdZ2jQoEFFhwBcNmrUqKEaNWpUdBgAAC/G9GnAixw6dEhz5syRn5+f/vOf/5SYEEtS165dNX/+fLvyxMREDRs2TK1bt1ZsbKwGDBiguXPnljjVunhKZUZGhqZNm6Zu3bqpadOmmj17tiRp9uzZio6O1rfffquVK1dqyJAhatmypd00zJ9++kn333+/OnbsqGbNmum6667Tk08+qePHj1/QPefm5uqdd97RmDFj1LVrVzVr1kzt2rXTqFGjtG7dOpu63377raKjo3X48GEdPnxY0dHR1o/z1zaWNo347Nmzmjlzpnr37q2YmBi1bdtWd911lzZt2mRXt/has2fP1q5duzR27Fi1adNGzZs31+23365t27Zd0P391b59+zRu3Di1a9dOLVq00K233qoNGzaUWn/VqlUaPny42rRpo5iYGPXt21evvfaazdc0ISHBOn32u+++s2mX2bNnKzMzU82aNdMtt9xic+5z584pJiZG0dHR+vjjj22Ovffee4qOjtZHH31kU56amqqZM2eqb9++io2NVevWrTVy5Mi/fQ/Fir92KSkpmjJlijp16qRmzZqpX79+WrZsWekNe54L7SfFynut9evXa8yYMbrmmmvUrFkz9ejRQ9OnT1d6evoFxedIQkKCxo8fr+7duys2NlatWrXSLbfcohUrVtjUK17X+91330mSzX0OHz683N8vJ0+e1OTJk9W5c2c1btzYOhPF0RTmC+3T5/+f8lclrVGOjo7W8uXLJUndu3e3xv7X/4PK0ydzc3P19ttvKy4uTm3btlXz5s3VrVs33XvvvSX+PwAAuDQwUgx4kYSEBOXl5alfv36yWCxl1vX397d5PWvWLM2dO1eVK1dW//79FRwcrPXr12vWrFnasGGD5s+fb/ee3NxcjRgxQmlpaerYsaNCQ0MVFRVlU2fhwoXauHGjunbtqmuuuUZnz561Hvvoo4/05JNPyt/fX926dVOtWrW0f/9+LV26VF9//bU+/PBD1a5du8z7SEtL0/PPP6+WLVvq2muvVZUqVXTy5EmtXbtWY8eO1XPPPachQ4ZIkurUqaP4+HgtWrRIkjRy5EjreRo3blzmddLT03Xrrbfqt99+U0xMjEaOHKkzZ87os88+05133qmnn37aLmmUpJ9//lnz5s1TixYtNGTIEB05ckRffPGFRo0apY8//lhXXXVVmdc936FDh3TLLbfIYrFo6NChOnnypBITEzVmzBjNnDlT119/vU39xx9/XAkJCapVq5Z69eql8PBw/fjjj3r55ZeVlJSkhQsXytfXV40bN1Z8fLzmzJmjOnXqKC4uznqOdu3aKSQkRDExMdq+fbsyMjIUGhoqSdq2bZs1Md28ebNuvPFG6/s2b94sSerQoYO17PDhwxo+fLgOHz6sNm3aqHPnzsrOztbatWs1evRoTZ06VTfffPNF3UNJXyt/f3/17t1bubm5+vzzzzVp0iT5+PjY3F9JytNPynutOXPmaPbs2YqIiNA//vEPValSRXv27NGCBQv0zTff6IMPPrC278V6+umn1bBhQ7Vt21bVq1dXamqq1q1bp8cee0zJycl68MEHJUnh4eGKj4/X8uXLdfjwYcXHx9u0QXnaITU1VUOHDlVwcLB69eolk8mkqlWrOoy1vH26POLj4/XVV19p9+7dGjFihMLDwyVJYWFh1jrl7ZOPP/64Vq1aJYvFooEDByowMFAnTpzQ1q1btX79el177bUXHS8AwIUMAF5jxIgRhsViMT788MNyvW/btm2GxWIxrrvuOuPEiRPW8ry8POPuu+82LBaL8frrr9u8p2vXrobFYjFGjhxpZGZm2p3zlVdeMSwWi9G8eXPjl19+sTv++++/G02bNjV69OhhHDt2zObYpk2bjEaNGhnjxo2zKb/99tsNi8ViU5aTk2McPXrU7vzp6elGv379jLZt2xrZ2dl2sXft2rWU1jAMi8Vi3H777TZlU6ZMMSwWizFlyhSjsLDQWp6cnGy0atXKaNq0qXHw4EFr+ebNmw2LxWJYLBZj2bJlNudasmSJYbFYjKeeeqrUGM538OBB67n+9a9/2Rzbvn270aRJE6NNmzbG2bNnreXLli0zLBaLcd9999ndf/HX5q233nJ438Veeuklw2KxGGvXrrWWzZgxw2jcuLExYsQIo0uXLtbygoICo127dkb37t1tznH77bcb0dHRxqpVq2zK09LSjBtuuMGIiYkxTp48+bfvwWKxGJMmTTLy8/Ot5Xv37jUaN25s9O3bt8T7K8mF9JPyXCspKcmwWCzG0KFDjbS0NJtjxff6/PPPX3B8pdm/f79dWU5OjjFixAijSZMmdt9vJX1fne9C2+HRRx818vLy7I5PmDDBsFgsNt8fF9Oni7/mmzdvtrtG8fkmTJjg8NrnK0+fTE9PN6Kjo424uDibr3exlJSUEq8BAKh4TJ8GvMjJkyclqdwPtCme6nnvvfeqevXq1nJfX19NmDBBPj4+Wrp0aYnvnThxooKDg0s9980336wmTZrYlS9ZskR5eXmaPHmyXbwdOnRQt27dtHbtWmVkZJQZu7+/v2rVqmVXHhYWpptuuklpaWnasWNHmedwJDc3V5988omCg4P10EMPyWQyWY/Vq1dPw4cPV15ent0UYklq1aqVBg0aZFN20003ydfXV9u3by9XHGFhYbrvvvtsymJiYjRgwAClp6fryy+/tJa//fbb8vX11T//+U8FBgbavGfcuHGKiIjQypUrL/jaxSO+SUlJ1rKkpCQ1bdpUvXr10rFjx5ScnCxJ2rVrl1JTU21GiXfv3q3vvvtOvXr1Ur9+/WzOHR4ervHjxysnJ0erV6/+2/cQFBSkxx9/XGaz2VrWsGFDtWrVSvv27VNmZuYF37cj5bnW4sWLJUnPPvusddSy2KBBg9S4ceNyfU1KU7duXbsyf39/DRs2TPn5+TZfQ2fx8/PThAkT7EbtHSlPn3a28vZJk8kkwzDk7+8vHx/7X68qV67sslgBAH8P06cBOLRz505JUvv27e2O1a9fX7Vq1dKhQ4d09uxZm6mHAQEBDvcNjo2NLbH8xx9/lFS0hrWkpPX06dMqKCjQH3/8oWbNmpV5jb1792r+/PnasmWLTp48qZycHJvjF7o+uTTJycnKzs5Wq1atFBERYXe8ffv2ev3117Vr1y67YyXF7ufnp6pVq5Z7DWmTJk1KnFrbrl07LV++XDt37lRcXJyys7O1e/duVa5c2Tr19a/8/f21b9++C752ixYtFBgYaE2ozp49q507d2r06NHWfpOUlKT69etbp06f359++OEHSVJGRoZ13fn5UlJSJEm///67JP2te7jyyitLbKfiP56kp6crJCTkwm7cgfJc68cff5Sfn58+//xzff7553bvycvLU0pKis6cOfO3EqwjR47ozTffVFJSko4ePapz587ZHP+73w8lqVOnzgVNl/6rC+3TrlDePhkaGqquXbtq7dq1GjhwoHr16mV9TgBPqweASxtJMeBFqlevrn379pX7l97idb7njxL/9bxHjhxRenq6TVJctWpVm1HTklSrVq3E8tTUVEkq8YFf58vKyirz+I8//qiRI0eqoKBA7du3V7du3RQaGiofHx/t2rVLa9as+dt7Ml9I+0gqMcn964hgMV9fXxUWFpYrjtLasri8eFQ9PT1dhmEoJSVFc+bMKdc1SuPv76/WrVtr06ZNSklJ0bZt21RQUKAOHTqoQYMGql69ujZv3qzbbrtNSUlJMplMNklx8dd748aN2rhxY6nXKf56/517KKvNJamgoKBc53PWtVJTU5Wfn+/wfrKysi46KT548KAGDx6s9PR0tWnTRp06dVJoaKjMZrMOHz6s5cuXu2SP8tK+Nxy50D7tCuXtk5L00ksv6c0339SqVausiXRAQIB69+6tCRMmlHo/AICKRVIMeJHWrVtr8+bN2rx5s/XhUheiONE9depUiVMvi6dln58QS3KYEJdVp3h0aOvWrX/rwUKvv/66zp07p7ffflvXXHONzbG5c+dqzZo1F33uYue3T0lKax9nK+36xeXF7Vj8b5MmTaxP33WG9u3ba+PGjUpKStIPP/yggIAAtWrVynps/fr1ys3N1datW3X11VfbjBwWt83kyZM1YsQIh9dy1T1UpNDQUBmGYX3asyssXLhQqampmjZtmt20/VWrVrmsLS/k/4KSXGifPv8aJf1R4/wH+F2o8vZJSQoMDNT48eM1fvx4HT16VFu2bNHy5cv1ySef6PDhw3rvvffKHQcAwPVYUwx4kUGDBsnPz0+rV6/Wb7/9Vmbd80eLip8kW9JWJ/v379exY8cUFRVV6qjYxWjRooUk6fvvv/9b59m/f78iIiLsEmJJpSYfPj4+5RotrF+/voKCgrR79+4SR4OL262ktdPOtHPnzhJHzorvs/j6ISEhuvrqq7V3717raNiFcNQu50+T3rx5s1q2bKmAgABJRWuOU1NT9d577ykrK8tuKn7x9mAX+vW+2HtwpvL2E0datGihtLQ07d2712nn/Kv9+/dLknr16mV3rKzvB6n0EXRnt8P5LrRPS1KlSpUkSUePHrWr//PPP5d4/uJ7K2lWRnn75F9FRkbqhhtu0Pz583XllVdq69atOnPmzEWdCwDgWiTFgBeJiopSfHy88vLyNHbs2FIfMPXNN99o9OjR1tc33XSTpKJR1+J1dFLRL8nTp09XYWGhBg8e7NRYhw0bJj8/P02bNs36gKbz5ebmXtAvq3Xq1FFqaqp2795tU7506dJS976NiIhQSkqK3VrL0vj7+2vAgAHKzMzUyy+/bHPswIEDWrx4sfz8/DRw4MALOt/FOnv2rF599VWbsh07dmjlypUKCwtTz549reWjRo1SXl6eJk2aVGIin5aWpl9++cWmLCIiQseOHSv1+k2bNlVYWJjWrFmjvXv32jxIqzgJ/s9//mPzulhMTIzatGmjL7/80m7v4mK//vqrTp8+/bfuwZnK208cGTVqlCRpypQpJS5xyMrKsq61v1h16tSRZJ8Ar1+/vtR2L14nf+TIkVKPO7MdzleePl38fIKEhATl5+dby48ePWp3jvNjl0q+t/L2yZSUFP366692dbKyspSVlSVfX1/5+fmVdbsAgArC9GnAy9xzzz3Kz8/Xq6++qsGDB6tly5Zq1qyZQkJCdOrUKX3//fd2D69q1aqVRo8erXnz5ql///7q3bu3goKCtH79eu3Zs0etW7fWXXfd5dQ4GzRooOeff16TJ09W//791blzZ9WrV0/5+fk6cuSItm7dqsqVK5f4QKLzjRw5Uhs2bNBtt92mvn37KiwsTD///LO2bt2q3r172zzNuFiHDh20Y8cOjR49Wm3atJG/v78aNWqkbt26lXqdhx9+WN9//73eeecd7dixQ9dcc411n+LMzExNmTJFV1xxxd9ul7K0bdtWH330kbZv365WrVpZ93QtLCzU1KlTbaaaDh48WL/88ovee+899ezZU506dVJkZKTS0tJ06NAhbdmyRYMGDdLUqVNt2uXTTz/VPffcoyZNmsjX11dt27ZV27ZtJUlms1nt2rWzTkk/PymuU6eO6tatqwMHDljr/dXMmTM1cuRITZ48WYsXL1bz5s0VFhamY8eOac+ePdqzZ48++OAD67Tri7kHZ7qYfuLofA8//LBmzZql3r17q0uXLoqKilJWVpaOHDmiLVu2qFWrVg7X2ZfltttuU0JCgh544AH17t1bNWrU0N69e7V+/Xr17dtXiYmJJcb1+eefa/z48bruuusUEBCg2rVrW/eddnY7nK88fbp58+Zq27attmzZoiFDhqh9+/Y6deqU1q5dq06dOpU4gtyhQwfNnz9fU6ZMUa9evRQSEqLw8HDdfvvtksrXJ48fP64bb7xRFotF0dHRioyMVEZGhv773//q5MmTGj58+N/eYxoA4BokxYAXio+PV9++ffXee+/p22+/VUJCgnJzcxUREaFGjRpp9OjRdqOajz76qJo0aaJ33nlHH3/8sfLz81W3bl09+OCDuvPOO+Xv7+/0OAcOHKhGjRpp4cKF+vbbb7VhwwYFBwerRo0a6t27t/r27evwHF26dNEbb7yh119/XYmJiTKbzYqNjdXbb7+tgwcPlpgU33vvvUpPT9fatWutD4yKi4sr85f8iIgIffDBB5o7d66+/PJLLVy4UIGBgYqNjdVdd92lTp06/a22uBBRUVF65plnNGPGDL3//vvKzc1VkyZNdN9996lz58529Z966il16dJF77//vjZt2qSzZ8+qUqVKioyM1F133aUbbrjBpv7kyZNlMpmUlJSkdevWqbCwUPHx8dakWCpKMtasWaPQ0FC7J2t36NBBBw4csI4o/1WtWrW0bNkyvfPOO/riiy+0cuVKFRQUqFq1amrYsKFuv/12WSyWv3UPznQx/cSRsWPHqlWrVlq8eLG2bt2qr7/+WqGh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bk5NTU2mTJlS8uQAAACglIoWxVOnTi1HHgAAABTRVFN02Jf3yF8UAACAqqUoBgAAoGoVHZ8GAADg/aFS7uhcSXSKAQAAqFqKYgAAAKqWohgAAICqZU0xAABAhSjUWlPc3nSKAQAAqFqKYgAAAKqW8WkAAIAK0VSjr9ne/EUBAACoWopiAAAAqpaiGAAAgKpV1jXFm/1BDU4HuunTHZ0B1e7TN3V0BlSz8/bo6AwAaAfNNbZkam+qVAAAAKqWu08DAADQ4V544YV8/etfz1tvvZU+ffrkwgsvzODBg1vFvP766znzzDMzY8aMLF26NF/4whcyZsyYJMn3v//93HvvvamtrU2XLl3y1a9+NTvvvHPR36soBgAAqBBN6bzj02eddVYOO+ywjBkzJnfeeWfOPPPMXH/99a1ivvWtb2WrrbbKD37wg8yZMycHHXRQ/vu//zsDBw7MiOrEFdMAACAASURBVBEj8rnPfS49evTI1KlT85nPfCYPP/xwunfvvsrfa3waAACAkmhoaMiMGTPaPBoaGlrFzZ49O08//XRGjx6dJBk9enSefvrpzJkzp1Xc1KlTl3V/+/Xrl8033zy//OUvkyQ777xzevTokSQZNmxYmpub89ZbbxXNUacYAACAkhg/fnwuv/zyNue//OUv57jjjlt2PHPmzAwYMCB1dXVJkrq6uqyzzjqZOXNm+vXrtyxuyy23zL333pvhw4dnxowZ+etf/5pBgwa1+fm/+MUvsuGGG2bdddctmqOiGAAAoEI0Vdjdp4888sgceOCBbc7X19f/Wz/v61//es4///yMGTMm6623XrbffvtlhfS//PnPf853v/vdXHvttav1MxXFAAAAlER9ff1qFcADBw7MrFmzUigUUldXl0KhkNdeey0DBw5sFdevX79ccskly47Hjh2bTTbZZNnxX//615xyyim54oorsvHGG69WjtYUAwAA0KHWWmutbLHFFpkwYUKSZMKECdliiy1ajU4nyZtvvpmlS5cmSSZNmpRnnnlm2TrkJ554Il/96lfzve99L1tuueVq/26dYgAAADrcuHHj8vWvfz1XXHFF6uvrc+GFFyZp6QYff/zxGT58eJ544ol885vfTG1tbfr27Zsrr7xy2c21zj777CxatChnnnnmsp950UUXZdiwYav8vYpiAACACtFU03mHfYcOHZpbb721zfkf/vCHy57vsssu2WWXXVb4/ttuu+3f+r2d9y8KAAAARSiKAQAAqFrGpwEAACpEpW3JVAl0igEAAKhaimIAAACqlqIYAACAqmVNMQAAQIUoWFPc7nSKAQAAqFqKYgAAAKqW8WkAAIAKYUum9qdTDAAAQNVSFAMAAFC1jE8DAABUiCZ9zXbnLwoAAEDVUhQDAABQtRTFAAAAVC1rigEAACpEsy2Z2p1OMQAAAFVLUQwAAEDVMj4NAABQIZqMT7c7nWIAAACqlqIYAACAqqUoBgAAoGpZUwwAAFAhmmJNcXvTKQYAAKBqKYoBAACoWsanAQAAKkRTjb5me/MXBQAAoGopigEAAKhaxqcBAAAqhLtPtz+dYgAAAKqWohgAAICqpSgGAACgallTDAAAUCGaaqwpbm86xQAAAFQtRTEAAABVy/g0AABAhSjYkqnd6RQDAABQtRTFAAAAVC1FMQAAAFXLmmIAAIAKYUum9qdTDAAAQNVSFAMAAFC1jE8DAABUiGZbMrU7nWIAAACqlqIYAACAqmV8GgAAoEI01ehrtjd/UQAAAKqWohgAAICqpSgGAACgallTDAAAUCGabMnU7nSKAQAAqFqKYgAAAKqW8WkAAIAKYXy6/ekUAwAAULUUxQAAAFQtRTEAAABVy5piAACACmFNcfvTKQYAAKBqKYoBAACoWsanAQAAKkShxvh0e9MpBgAAoGopigEAAKhaxqcBAAAqhLtPtz+dYgAAAKqWohgAAICqpSgGAACgallTDAAAUCGa9DXbnb8oAAAAVUtRDAAAQNUyPg0AAFAhmm3J1O50igEAAKhaOsXvI937JvtfkwzdK1nwRvKb05Inb2obV9c12fu7yeYHJnVdkml/SO75QjL3lfLnTGV7a8HSfOPOl/KH5xrSt+caOXGP9bPfiH5t4hoWLs03fzk9Dz3bkCQ5bLv+OW639Za9vvv/NzlvzGtMXW3LN5fbbNAr1352s/J8CDq/L30pOeqoZPjw5Kabkv/5n47OiM6ke+9k9InJkG2ThQ3JA9ckTz3QNq5br2SvY5Oh27UcP3Z38vsbWp7X90+OuaZ1fNceyf1XJY/8vLT5U9lcf/C+oCh+H9n3+0lhSXLJgGTdDyaH3ZPMejx5/enWcR85IRm0fXLliGTR28l+Vyf7XJbccnDH5E3lOueeaelSV5M/nDIiU15dmGN+8o9svm6PbLpOj1ZxF0yckYWNTfntV4Zn9vzGHDX+mazXp2sO3mbtZTFXHrZJdhhaX+6PQDV45ZXkvPOSUaOSHj2Kx8N7sfdxSWFp8p1PJQOGJod8M5n1fPLGS63j9vxi0qV7cvkRSa8+yeEXJW+/ljxxX9LwenLx/stjP7Bucux1ydTfl/WjUIFcf/C+sFrj0/PmzctTTz1V6lyqWpeeyX8dnDzw/5LG+cn0PyR/vysZcUTb2L5DkufuS+a/lhQWJ0/dnPTfsvw5U9kWLCnkV1Peygm7r5de3ery4Y3WzO7D+uTOx2e3if3tM2/l8zutmx5dazOob7d84kNr57a/tI2DkrjjjuTOO5PZrjnaWZfuyeY7JQ9elzQuSmY8lfxjUjJ8j7axm45MJt2cLF2cvD0r+dvEZOtRK/65I/ZIpk1uiYOVcf3xb2pKTUU9KkHRovjBBx/Mxz/+8Rx33HFJksmTJ+cLX/jCKt/T0NCQGTNmtHmwcmttljQtTeb8Y/m5WY+vuNj9yzXJBjsmaw5M1uiRDD88efaX5cuVzuHF2YtTV5sMWbv7snObr9sjz762aMVvaH7H0+bkH68tbPXyybe9kJEXPp7PXf9Mpr66oBQpA7SvfusnTYVkzsvLz816Lum/0Yrja2paP+8/eMVxw/dMJv+63dKkk3L9wftG0aL4e9/7Xn7+85+nvr5lLHL48OGZNm3aKt8zfvz4fOxjH2vzYOW6rpksbmh9bvHbSbfebWPn/CNpmJ6c9EpyWkOy9hbJg+eUJ086jwVLClmzW12rc7271WX+kkKb2J03+UCufvjVzFtcyEuzF+W2v76RhY1Ny16/+OAh+e1Xh+eBrw7PRwb3zv/e8I80LFxa8s8A8B/p2iNZ/K4v8RbPT7r2bBv73P8l2x/a8p6+67V06bp0axu3wVZJr77JlIdKkzOdh+sP3jdWa01x//79Wx137dp1lfFHHnlkDjzwwDbnr9ngPWRWZZbMS7q9azlmt/pk8dy2sft+P6nrllzYr2XUesdTk8N/mVwzsjy50jn07FqXeYtbF8DzFjelV9e6NrFn7LNBzr13ekZ978n06bFGPj68X+6ZPGfZ69tuuOay58d8dGDueHx2Hp02L7sP61O6DwDwn1qyMOn2rgKkW69kyQqmXX51RTLqS8kXr2u5IdJTDyRb7tY2bsReLWs5G1cydQP/4vrj31QpI8mVpGhR3KtXr7zxxhup+efIxiOPPJLevVfQvnyH+vr6ZZ1lVs/sZ5LaNZJ+myRznm05N2Dr5PUVLOVe94PJb7+RLHqz5fiRy5Ldzk16rJUstOSO1TR4rW4pNCUvzl6UwWu1jFBPnbUgm6zTvU1sn55r5NJPDFl2/O37X86I9Xut9GfXpCbNzSt9GeD9Yc7LSW1d0nf95M1/jrCus3Hy+kttYxfNTe781vLjXT+XvPL31jFrdE02/2jy83ElS5lOxPUH7xtFx6dPOumkjB07NjNmzMgRRxyRk08+OV/72tfKkVtVaVyQTLk92fWclptubbBDMmxM8sQNbWNf/r9kxGdbOsm1ayTbHZs0vKwg5r3p2bUue27RJ9/77StZsKSQx6bNy2+mvpUxW6/VJnbanMV5c8HSFJqa8+A/3s7Nj72eL+4yMEnyyltL8ti0eVmytCmLG5vyo4dfzZsLluZD7+gew3+kri7p1q3l33c+h/9U46Jk6sPJLke23PRo0JbJZjskk+9vG9tnYNKjd1JT27Itzjb7Jg//pHXMsB1bipeX/lae/Klsrj943yjaKd56661z/fXX5y9/+UuSZJttttEFLpF7jk3GXJuc/FpLgXvPF1u2Y9pwp5bx6Av+2aD/9cnJ3t9LjvtHy57Frz2Z3Nx2Wh2KOuvjG+b0O1/MDhc9kT496zJu9EbZdJ0eefSluRl747P56ze2SZI8+cr8nD9xRuYuWprBa3XPJQcPWbZt0/wlhYybMC3T5yxOtzVqsvm6PfPDz2ySvj3t+EY7OeOMZNy45cdHHNFyfPbZHZURncnEy5LRJyVfuSVZODeZ+N2W7XA22Co59PzlW90M3DTZ89ike6+WDt+d32q7bc7wvZInV1DQwMq4/vg3GJ9ufzXNzSsfciwUCvnEJz6RO+64o11+2dn++9GBzrrpsI5OgWr36Zs6OgOq2Xkr2OYFoJp8o3PclfvMVNa2M+dkn45OoahVjk/X1dWlZ8+eWbx4cbnyAQAAgLIpOt84ZMiQHH744Rk1alR69lx+h7zDDz+8pIkBAABAqRUtiguFQjbddNM8//zz5cgHAACAlShYU9zuihbFF1xwQTnyAAAAgLIrWhQ3Nzfn5ptvzh//+MckyU477ZRPfvKTy/YtBgAAgEpVtCi+6KKLMmXKlBx00EFJkl/84hd58cUXc+qpp5Y8OQAAAJZrNj7d7ooWxQ8//HDuuOOOrLFGS+g+++yTgw46SFEMAABAxVvllkz/8s5RaWPTAAAAdBZFO8U77bRTxo4dmwMPPDBJy/j0TjvtVPLEAAAAoNSKFsWnnHJKbr755vz6179Okuyxxx455JBDSp4YAAAArTVZU9zuihbFtbW1+fSnP51Pf/rT5cgHAAAAyqbomuLjjjsub7311rLjN998MyeccEJJkwIAAIByKNopnj59evr06bPsuG/fvpk2bVpJkwIAAKCtQnOFjU9XQLpFO8WFQiGFQmHZcWNjY5YsWVLSpAAAAKAcVuvu01/96lfz2c9+Nkly/fXXZ+eddy55YgAAAFBqRYviE088MVdddVW+9a1vJUl23XXXHH300SVPDAAAgNbcfbr9FS2Ku3Tpki9/+cv58pe/XI58AAAAoGyKrin+8Y9/nLlz5yZJTj311Oy99955+OGHS54YAAAAlFrRovj2229P796986c//SmzZ8/O+eefn29/+9vlyA0AAABKquj4dF1dXZLkkUceyX777ZcPfehDaW5uLnliAAAAtNZsTXG7K9op7t69e66++urcc8892XHHHdPc3JzGxsZy5AYAAAAlVbQovuCCC/L666/n5JNPTv/+/TN9+vTst99+5cgNAAAASqro+PSQIUPyjW98Y9nxhhtumGOOOaakSQEAANBWU/G+Ju+RvygAAABVS1EMAABA1So6Pg0AAMD7Q1Nzhd19ugLSLVoUP/jgg23Orbnmmtlss83Su3fvkiQFAAAA5VC0KL7iiivy5JNPZrPNNkuSPPPMMxk2bFhmzZqV8847L7vttlvJkwQAAIBSKLqmeMMNN8zNN9+cO+64I3fccUduueWWbLzxxrn++uvzne98pxw5AgAAQEkU7RRPnTo1W2211bLjLbfcMs8880yGDh2a5ubmkiYHAADAcoVKWKRbYYp2inv06JEJEyYsO54wYUK6d++eJKmp8R8EAACAylW0U3zBBRfklFNOyWmnnZaamppssskmufDCC7NgwYKceuqp5cgRAAAASqJoUTx06NDcfvvtmTdvXpKWO0//y4477li6zAAAAGiludK2ZKoAq7VP8bRp0zJt2rQUCoVl53bZZZeSJQUAAADlULQovvTSS3Prrbdm6NChqa1tWYJcU1OjKAYAAKDiFS2KJ06cmPvvv7/V2DQAAAB0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zZuXa665JlOmTMmSJUuWnb/22mtLmhgAAACUWtEbbZ1++ulZunRpnn322ey///5pbGzM5ptvXo7cAAAAeIfmppqKelSCokXxiy++mJNOOik9evTIAQcckB/96Ef5y1/+Uo7cAAAAoKSKFsXdunVLknTp0iVvv/12unbtmjfffLPkiQEAAECpFV1TvMEGG+Stt97Kvvvum0MPPTT19fUZNmxYOXIDAACAkipaFH/7299Oknz+85/PVlttlXnz5mWXXXYpeWIAAAC01lQh63QrSdGi+F8KhUI+9KEPJUmam5tLlhAAAACUS9Gi+P7778/555+fmTNnJmkpiGtqajJlypSSJwcAAAClVLQovuCCC3LppZdmyy23TF1dXTlyAgAAYAUKTR2dQedTtCju379/ttlmm3LkAgAAAGVVtCg+7LDDctlll2XPPfdctj1TkgwZMqSkiQEAAECpFS2K58yZk2uuuSY333zzsvHpmpqa/O53vyt1bgAAALyDu0+3v6JF8fjx43PfffdlwIAB5cgHAAAAyqa2WMDAgQMVxAAAAHRKRTvFH/zgB3PKKadk7733brWmeKeddippYgAAAFBqRYviv/3tb0mSa665Ztm5mpoaRTEAAECZNResKW5vRYvin/70p+XIAwAAAMqu6JpiAAAA6KyKdooBAAB4fyg0dXQGnY9OMQAAAFVLUQwAAEDVWun49IknnpiampXf2ezSSy8tSUIAAABQListirfffvty5gEAAEARTU22ZGpvKy2KP/nJT5YzDwAAACi7onefLhQKueOOOzJ16tQsXrx42flzzz23pIkBAABAqRW90dZZZ52VSZMm5de//nXWXXfdPPbYY6mtdX8uAACAcmtqqqxHJSha3T7++OO55JJLUl9fny996Uu56aab8vzzz5cjNwAAACipokVx165dU1NTk7q6uixatCgf+MAHMnv27HLkBgAAACVVdE1xnz590tDQkB133DHHHHNM+vbtm/79+5cjNwAAAN6hxt2n213RovgHP/hBunbtmhNPPDF33nlnGhoacvDBB5cjNwAAACipouPTN954Y5Kkrq4uBx10UI466qjceuutJU8MAAAASq1oUXz33Xev1jkAAACoNCsdn540aVL++Mc/5vXXX8+3v/3tZefnzp2bpkq5tzYAAEAnUlewpri9rbQo/tcdp5O02pd4/fXXz+c+97nSZwYAAAAlttKieOTIkRk5cmT23nvvbL755uXMCQAAAMqi6N2nhwwZku985zuZNGlSkizbmqlbt24lTw4AAIDlaq1kbXdFb7R17rnnZsaMGTnppJNy0kknZcaMGTn33HPLkRsAAACUVNFO8eOPP97qbtPbbbdd9t9//5ImBQAAAOVQtFOcJAsXLlzhcwAAAKhkRTvFH//4x3PooYdm9OjRSZJ77703++23X8kTAwAAoLXaJlsytbeiRfEXvvCFDBs2LH/84x+TJMcff3x22223kicGAAAApbbSovj000/P+eefnyTZbbfdFMIAAAB0OistiqdMmVLOPAAAACiiptDRGXQ+q3WjLQAAAOiMVtopfuaZZ7L99tu3Od/c3JyamppMmjSppIkBAABAqa20KB48eHCuvvrqcuYCAADAKtS5+3S7W2lR3LVr16y//vrlzAUAAADKaqVrirt06VLOPAAAAKDsVloU33LLLeXMAwAAAMpupePTAAAAvL/UNnV0Bp2PLZkAAACoWopiAAAAqpbxaQAAgApRW7AlU3vTKQYAAKBqKYoBAACoWopiAAAAqpY1xQAAABWipsma4vamUwwAAEDVUhQDAABQtYxPAwAAVIi6Qkdn0PnoFAMAAFC1FMUAAABULePTAAAAFaLW3afbnU4xAAAAVUtRDAAAQNVSFAMAAFC1rCkGAACoELW2ZGp3OsUAAABULUUxAAAAVcv4NAAAQIWosSVTu9MpBgAAoGopigEAAKhaimIAAACqljXFAAAAFaLOlkztTqcYAACAqqUoBgAAoGoZnwYAAKgQtU0dnUHno1MMAABAh3vhhRdyyCGHZNSoUTnkkEPy4osvtomZPXt2jj766Oy3337ZZ599Mm7cuCxdurRVzPPPP5+tt946F1544Wr9XkUxAAAAHe6ss87KYYcdlvvuuy+HHXZYzjzzzDYxV155ZYYOHZq77747d911V5566qn86le/WvZ6oVDIWWedlT322GO1f6+iGAAAoELUFmoq6rG6Zs+enaeffjqjR49OkowePTpPP/105syZ0yqupqYm8+fPT1NTU5YsWZLGxsYMGDBg2etXX311dt111wwePHj1/6arHQkAAADvQUNDQ2bMmNHm0dDQ0Cpu5syZGTBgQOrq6pIkdXV1WWeddTJz5sxWcccee2xeeOGF7LTTTsse2267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JcWlc6xatUrjxo2rinBdNmHCBL3//vvVek78Pj179lSfPn305z//Wf3799fGjRtrOiQlJCQoOzu7psMAai2vmg6grtqzZ49Onz6t++67r6ZDsZSUlMjLiyJxJXLXtZk1a1aVH9MdnE6nbDabbDZbTYcCF5SUlOjBBx/Ugw8+KEn66aeftGLFCkVERFjbxMfH11R4l4T74pVj1apVkkr/yDJo0CCtW7fOpf12794th8Ohrl27ujO8y+JwOGo6BFymRYsWKSgoSP/97381ZMgQdenSRddff32l+7nrefbOO++oa9euatKkSZUeF6greNJfhlatWum5557T559/rpycHL3yyitKSUnR9u3bVVJSon/84x8KCAhQVlaWxo8fr8LCQtntdvXo0UMTJ07UwYMH9cEHH8jpdColJUX9+vVT3759JUkLFizQtm3bdObMGc2aNUv33nvvBedfsWKFEhISVL9+fTmdTi1cuFABAQFKTU3VrFmzlJWVJUkaOXKkwsPDlZ6ermnTpunUqVPy8vLSuHHjdP/991ufZezYsdq6dau6d++u5557TnFxcfrss8/kcDh00003aebMmfL396++LxiSLu3a7Nq1SwsXLpTdbpfD4dDo0aPVr18/SdIPP/ygyZMn6/Tp0woKCpLdbrfOERkZqZEjRyo0NFSTJk1S/fr1deTIEZ04cULt27fX3LlzZbPZlJmZqYkTJ+qXX35Rs2bNJEn33XexwXmwAAAOq0lEQVSfhg0bVibm7OxsRUVFWX+t7tKli6KjoyVJb731ljZs2CCbzSZvb28lJSXJw8NDcXFx+uijjyRJd911l6ZMmSIfHx8tXrxYhw8fVkFBgX7++WetWLFC2dnZmj17tn799VcVFxdrxIgRGjRokNuvRV32wQcf6ODBg3rppZe0b98+Pfroo1q1apWCg4M1ffp0tWnTRhEREReU19tuu01bt27VokWL9PLLL+vYsWMKCwvT7bffrkWLFqlnz56KjY1VUFCQIiMj1bZtW33zzTc6efKkHn74YU2YMEHS/8rvmTNn1Lp1a2VkZGjMmDEKDQ0tE+ePP/5obed0OhUeHq4nnnhCRUVFWrBggbZv3y4PDw81a9ZMb7zxhhwOh+bPn6/t27dLkrp3764JEybI09NTkyZNkqenp9LS0lRYWKh169bp22+/1fz581VYWChJeuaZZ/TA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dF39rYsd57eWLFmi/fv3a/fu3Ro+fLimT5+uP/zhD5f9Wc5V/CTJGKMxY8Zo8ODBl308VB1Xr8306dPVs2dPLVmyRDabTb17966wrF3MuXItSZ6enpc83q1Dhw5au3atUlJStG7dOsXFxf2uCWR8fHys/xtj1LhxY5fHEaLqhISE6IsvvlB2drY6d+6smTNnauvWrRdU0s8vr5eqorLnyti73r17q3379tq5c6fi4+P14Ycfav78+Zcdz29/91q1aqXExMTLPh6uHOvWrdO+ffuUlJQkHx8fLVmyRMePH3dp398+p88te3iUzlvqdDq1e/durV69WklJSbr++uuVnJys5ORka7/yfk9at26tr776Sj/++KOVMPft21f33HOPduzYodjYWCUnJ+vVV1+97M+NqnVuTPE5K1asqLD+dP7z7GLOjTdevXr1Rbvzu/qcrqxeUN591ZXzA1crZp92o/z8fPn7+6tBgwbKzMzU5s2brZ/5+voqPz//ko9ZUlKio0ePKjg4WE8++aS6deum77//Xs2bN5eXl5c+/vhja9tff/1Vvr6+atOmjdauXStJSk1N1YEDB9S+fftyj9+zZ08lJSUpNzdXklRUVKQDBw5ccpyoehVdm/z8fDVt2lQ2m007d+5Uenq6pNJyFhQUpPXr10uS9u3bp0OHDl3yuTt16mSVoePHj2v37t3lbnf06FH5+vqqX79+mjx5sr777js5nU6Fhobq/fffV0FBgaTSsimVjjn++OOPVVBQIGOMVq9efdHJcJo3b66GDRuWqVympqZax4T7hISEKD4+Xh06dJAk3X333YqPj79oj4Hf8vX1vazr5Ovrq5YtW1rjRL/77ruLlt/09HT5+/vrkUce0dNPP639+/dLKu3Fs3z5chUVFUmS1QLSpUsXJScnq7i4WMXFxUpOTr5o2evQoYPS09PLlPt9+/bJGHPJnwnu0bVrV23cuFGFhYUX3Et++7zNz89X48aN5ePjo9zc3CqfOTg/P19+fn667rrrZLfb9eGHH1a6z1133aVFixYpKirKeiPAkSNH5O/vr0GDBumpp57Svn37qjROVK1LqT9VVGe75557FBcXZ60/fvy4Ne64Ij4+PheU84vVCy52X/095wdqO1qK3SgyMlLPPvus+vfvr5tuuqlMBfKhhx5ScnKywsLCyky0VRmn06lJkyYpPz9fNptNt9xyi6KiouTl5aWlS5fq5Zdf1tKlS2Wz2TRy5EgNHDhQ8+fP17Rp05SQkCAvLy/FxMRcdIbEgQMHKicnx5pAyRijoUOHqnXr1r//C8HvUtG1iYqK0owZM7R48eILupjGxMRo8uTJio+PV1BQ0GV193zxxRc1ceJErV+/XrfeequCg4PL7Va/Z88eJSQkyMPDQ06nUzNmzJCHh4cGDhyozMxMRUREyMvLS97e3kpMTFSPHj108OBBDRkyRFJpF8QxY8aUG4OXl5diY2M1e/Zs/fOf/5TT6VSTJk20cOHCS/48uDQhISGaOHGidQ8LCQnRihUrrC7KlWnVqpWaN2+u/v37q0WLFlq0aJHL5547d66io6MVFxenoKAgBQUFyc/P74LtPv74Y61fv1716tWTzWazJnh78skn9dprr2ngwIGqV6+eNdFXRESEMjIyrK6O9913nx577LFyY2jUqJGWLl2qefPmafbs2SouLlazZs0UGxvLjOhXiJ49e+rQoUPWDOfBwcHW5EC9e/fW2LFjFRYWpgEDBujRRx/Vli1b1KdPH91www3q2LFjlc4C3aNHD61fv159+vRR48aNdffdd+v777+vdL82bdrozTff1JgxYzRjxgzt3btXmzZtuqBM48p0KfWnyupsc+bMsbo3+/j4aNasWZVOeDp8+HBFR0erYcOGeu211yqsF1R0X73c8wO1nc3wp24AlTh79qy8vLzk5eWlkydPavDgwUpISFCLFi1qOjRc5QoLC+Xt7S2bzaYffvhBkZGR+uSTT1weAwoAKIv7KnAhWooBVOrIkSN64YUXZIxRSUmJxo4dS0KMarF3717FxMRYXZVnzpxJxQ0Afgfuq8CFaCkGAAAAANRZTLQFAAAAAKizSIoBAAAAAHUWSTEAAAAAoM4iKQYAAAAA1FkkxQAAAACAOoukGAAAAABQZ/0f/9A3G3/ZVu4AAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 1296x1152 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.rcParams['figure.figsize'] = (18,16)\n",
    "sns.heatmap(data.corr(),cmap='rainbow',annot= True)\n",
    "plt.title('Correlation between the  attributes', fontsize =20)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Preprocessing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T21:23:44.038299Z",
     "iopub.status.busy": "2022-01-05T21:23:44.037926Z",
     "iopub.status.idle": "2022-01-05T21:23:44.046494Z",
     "shell.execute_reply": "2022-01-05T21:23:44.045644Z",
     "shell.execute_reply.started": "2022-01-05T21:23:44.038215Z"
    }
   },
   "outputs": [],
   "source": [
    "from sklearn import preprocessing\n",
    "le = preprocessing.LabelEncoder()\n",
    "\n",
    "#label encoding for test preparation course \n",
    "data['test preparation course'] = le.fit_transform(data['test preparation course'])\n",
    "#label encoding for lunch\n",
    "data['lunch'] = le.fit_transform(data['lunch'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T21:26:29.195513Z",
     "iopub.status.busy": "2022-01-05T21:26:29.194936Z",
     "iopub.status.idle": "2022-01-05T21:26:29.213032Z",
     "shell.execute_reply": "2022-01-05T21:26:29.211758Z",
     "shell.execute_reply.started": "2022-01-05T21:26:29.195453Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3    319\n",
       "4    262\n",
       "2    190\n",
       "5    140\n",
       "1     89\n",
       "Name: race/ethnicity, dtype: int64"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['race/ethnicity'] = data['race/ethnicity'].replace('group A',1)\n",
    "data['race/ethnicity'] = data['race/ethnicity'].replace('group B',2)\n",
    "data['race/ethnicity'] = data['race/ethnicity'].replace('group C',3)\n",
    "data['race/ethnicity'] = data['race/ethnicity'].replace('group D',4)\n",
    "data['race/ethnicity'] = data['race/ethnicity'].replace('group E',5)\n",
    "data['race/ethnicity'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T21:28:16.998171Z",
     "iopub.status.busy": "2022-01-05T21:28:16.997813Z",
     "iopub.status.idle": "2022-01-05T21:28:17.009432Z",
     "shell.execute_reply": "2022-01-05T21:28:17.008052Z",
     "shell.execute_reply.started": "2022-01-05T21:28:16.998121Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4    226\n",
       "0    222\n",
       "2    196\n",
       "5    179\n",
       "1    118\n",
       "3     59\n",
       "Name: parental level of education, dtype: int64"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['parental level of education'] = le.fit_transform(data['parental level of education'])\n",
    "data['parental level of education'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T21:28:39.564524Z",
     "iopub.status.busy": "2022-01-05T21:28:39.564127Z",
     "iopub.status.idle": "2022-01-05T21:28:39.609086Z",
     "shell.execute_reply": "2022-01-05T21:28:39.608117Z",
     "shell.execute_reply.started": "2022-01-05T21:28:39.564465Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>race/ethnicity</th>\n",
       "      <th>parental level of education</th>\n",
       "      <th>lunch</th>\n",
       "      <th>test preparation course</th>\n",
       "      <th>math score</th>\n",
       "      <th>reading score</th>\n",
       "      <th>writing score</th>\n",
       "      <th>Total marks</th>\n",
       "      <th>Percentage</th>\n",
       "      <th>Grade_math</th>\n",
       "      <th>Grade_reading</th>\n",
       "      <th>Grade_writing</th>\n",
       "      <th>Overall_grade</th>\n",
       "      <th>pass_math</th>\n",
       "      <th>pass_reading</th>\n",
       "      <th>pass_writing</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>female</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>72</td>\n",
       "      <td>72</td>\n",
       "      <td>74</td>\n",
       "      <td>218</td>\n",
       "      <td>72.666667</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>Pass</td>\n",
       "      <td>Pass</td>\n",
       "      <td>Pass</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>female</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>69</td>\n",
       "      <td>90</td>\n",
       "      <td>88</td>\n",
       "      <td>247</td>\n",
       "      <td>82.333333</td>\n",
       "      <td>D</td>\n",
       "      <td>A</td>\n",
       "      <td>B</td>\n",
       "      <td>B</td>\n",
       "      <td>Pass</td>\n",
       "      <td>Pass</td>\n",
       "      <td>Pass</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>female</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>90</td>\n",
       "      <td>95</td>\n",
       "      <td>93</td>\n",
       "      <td>278</td>\n",
       "      <td>92.666667</td>\n",
       "      <td>A</td>\n",
       "      <td>A</td>\n",
       "      <td>A</td>\n",
       "      <td>A</td>\n",
       "      <td>Pass</td>\n",
       "      <td>Pass</td>\n",
       "      <td>Pass</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>male</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>47</td>\n",
       "      <td>57</td>\n",
       "      <td>44</td>\n",
       "      <td>148</td>\n",
       "      <td>49.333333</td>\n",
       "      <td>F</td>\n",
       "      <td>E</td>\n",
       "      <td>F</td>\n",
       "      <td>F</td>\n",
       "      <td>Pass</td>\n",
       "      <td>Pass</td>\n",
       "      <td>Pass</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>male</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>76</td>\n",
       "      <td>78</td>\n",
       "      <td>75</td>\n",
       "      <td>229</td>\n",
       "      <td>76.333333</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>Pass</td>\n",
       "      <td>Pass</td>\n",
       "      <td>Pass</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   gender  race/ethnicity      ...       pass_reading  pass_writing\n",
       "0  female               2      ...               Pass          Pass\n",
       "1  female               3      ...               Pass          Pass\n",
       "2  female               2      ...               Pass          Pass\n",
       "3    male               1      ...               Pass          Pass\n",
       "4    male               3      ...               Pass          Pass\n",
       "\n",
       "[5 rows x 17 columns]"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T21:33:06.668336Z",
     "iopub.status.busy": "2022-01-05T21:33:06.667783Z",
     "iopub.status.idle": "2022-01-05T21:33:06.676659Z",
     "shell.execute_reply": "2022-01-05T21:33:06.675866Z",
     "shell.execute_reply.started": "2022-01-05T21:33:06.668261Z"
    }
   },
   "outputs": [],
   "source": [
    "#encoding for gender\n",
    "data['gender'] = le.fit_transform(data['gender'])\n",
    "#encoding for pass math\n",
    "data['pass_math'] = le.fit_transform(data['pass_math'])\n",
    "#encoding for pass reading\n",
    "data['pass_reading'] = le.fit_transform(data['pass_reading'])\n",
    "#encoding for pass reading\n",
    "data['pass_writing'] = le.fit_transform(data['pass_writing'])\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T21:50:47.588257Z",
     "iopub.status.busy": "2022-01-05T21:50:47.587654Z",
     "iopub.status.idle": "2022-01-05T21:50:47.632751Z",
     "shell.execute_reply": "2022-01-05T21:50:47.632065Z",
     "shell.execute_reply.started": "2022-01-05T21:50:47.588207Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>race/ethnicity</th>\n",
       "      <th>parental level of education</th>\n",
       "      <th>lunch</th>\n",
       "      <th>test preparation course</th>\n",
       "      <th>math score</th>\n",
       "      <th>reading score</th>\n",
       "      <th>writing score</th>\n",
       "      <th>Total marks</th>\n",
       "      <th>Percentage</th>\n",
       "      <th>Grade_math</th>\n",
       "      <th>Grade_reading</th>\n",
       "      <th>Grade_writing</th>\n",
       "      <th>Overall_grade</th>\n",
       "      <th>pass_math</th>\n",
       "      <th>pass_reading</th>\n",
       "      <th>pass_writing</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>72</td>\n",
       "      <td>72</td>\n",
       "      <td>74</td>\n",
       "      <td>218</td>\n",
       "      <td>72.666667</td>\n",
       "      <td>3</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>69</td>\n",
       "      <td>90</td>\n",
       "      <td>88</td>\n",
       "      <td>247</td>\n",
       "      <td>82.333333</td>\n",
       "      <td>4</td>\n",
       "      <td>A</td>\n",
       "      <td>B</td>\n",
       "      <td>B</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>90</td>\n",
       "      <td>95</td>\n",
       "      <td>93</td>\n",
       "      <td>278</td>\n",
       "      <td>92.666667</td>\n",
       "      <td>1</td>\n",
       "      <td>A</td>\n",
       "      <td>A</td>\n",
       "      <td>A</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>47</td>\n",
       "      <td>57</td>\n",
       "      <td>44</td>\n",
       "      <td>148</td>\n",
       "      <td>49.333333</td>\n",
       "      <td>6</td>\n",
       "      <td>E</td>\n",
       "      <td>F</td>\n",
       "      <td>F</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>76</td>\n",
       "      <td>78</td>\n",
       "      <td>75</td>\n",
       "      <td>229</td>\n",
       "      <td>76.333333</td>\n",
       "      <td>3</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   gender  race/ethnicity      ...       pass_reading  pass_writing\n",
       "0       0               2      ...                  1             1\n",
       "1       0               3      ...                  1             1\n",
       "2       0               2      ...                  1             1\n",
       "3       1               1      ...                  1             1\n",
       "4       1               3      ...                  1             1\n",
       "\n",
       "[5 rows x 17 columns]"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Grade_math'] = data['Grade_math'].replace('O',0)\n",
    "data['Grade_math'] = data['Grade_math'].replace('A',1)\n",
    "data['Grade_math'] = data['Grade_math'].replace('B',2)\n",
    "data['Grade_math'] = data['Grade_math'].replace('C',3)\n",
    "data['Grade_math'] = data['Grade_math'].replace('D',4)\n",
    "data['Grade_math'] = data['Grade_math'].replace('E',5)\n",
    "data['Grade_math'] = data['Grade_math'].replace('F',6)\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T21:50:51.136215Z",
     "iopub.status.busy": "2022-01-05T21:50:51.135538Z",
     "iopub.status.idle": "2022-01-05T21:50:51.183825Z",
     "shell.execute_reply": "2022-01-05T21:50:51.182434Z",
     "shell.execute_reply.started": "2022-01-05T21:50:51.136147Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>race/ethnicity</th>\n",
       "      <th>parental level of education</th>\n",
       "      <th>lunch</th>\n",
       "      <th>test preparation course</th>\n",
       "      <th>math score</th>\n",
       "      <th>reading score</th>\n",
       "      <th>writing score</th>\n",
       "      <th>Total marks</th>\n",
       "      <th>Percentage</th>\n",
       "      <th>Grade_math</th>\n",
       "      <th>Grade_reading</th>\n",
       "      <th>Grade_writing</th>\n",
       "      <th>Overall_grade</th>\n",
       "      <th>pass_math</th>\n",
       "      <th>pass_reading</th>\n",
       "      <th>pass_writing</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>72</td>\n",
       "      <td>72</td>\n",
       "      <td>74</td>\n",
       "      <td>218</td>\n",
       "      <td>72.666667</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>69</td>\n",
       "      <td>90</td>\n",
       "      <td>88</td>\n",
       "      <td>247</td>\n",
       "      <td>82.333333</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>B</td>\n",
       "      <td>B</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>90</td>\n",
       "      <td>95</td>\n",
       "      <td>93</td>\n",
       "      <td>278</td>\n",
       "      <td>92.666667</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>A</td>\n",
       "      <td>A</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>47</td>\n",
       "      <td>57</td>\n",
       "      <td>44</td>\n",
       "      <td>148</td>\n",
       "      <td>49.333333</td>\n",
       "      <td>6</td>\n",
       "      <td>5</td>\n",
       "      <td>F</td>\n",
       "      <td>F</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>76</td>\n",
       "      <td>78</td>\n",
       "      <td>75</td>\n",
       "      <td>229</td>\n",
       "      <td>76.333333</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   gender  race/ethnicity      ...       pass_reading  pass_writing\n",
       "0       0               2      ...                  1             1\n",
       "1       0               3      ...                  1             1\n",
       "2       0               2      ...                  1             1\n",
       "3       1               1      ...                  1             1\n",
       "4       1               3      ...                  1             1\n",
       "\n",
       "[5 rows x 17 columns]"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Grade_reading'] = data['Grade_reading'].replace('O',0)\n",
    "data['Grade_reading'] = data['Grade_reading'].replace('A',1)\n",
    "data['Grade_reading'] = data['Grade_reading'].replace('B',2)\n",
    "data['Grade_reading'] = data['Grade_reading'].replace('C',3)\n",
    "data['Grade_reading'] = data['Grade_reading'].replace('D',4)\n",
    "data['Grade_reading'] = data['Grade_reading'].replace('E',5)\n",
    "data['Grade_reading'] = data['Grade_reading'].replace('F',6)\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T21:50:54.954382Z",
     "iopub.status.busy": "2022-01-05T21:50:54.953966Z",
     "iopub.status.idle": "2022-01-05T21:50:55.009652Z",
     "shell.execute_reply": "2022-01-05T21:50:55.008548Z",
     "shell.execute_reply.started": "2022-01-05T21:50:54.954294Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>race/ethnicity</th>\n",
       "      <th>parental level of education</th>\n",
       "      <th>lunch</th>\n",
       "      <th>test preparation course</th>\n",
       "      <th>math score</th>\n",
       "      <th>reading score</th>\n",
       "      <th>writing score</th>\n",
       "      <th>Total marks</th>\n",
       "      <th>Percentage</th>\n",
       "      <th>Grade_math</th>\n",
       "      <th>Grade_reading</th>\n",
       "      <th>Grade_writing</th>\n",
       "      <th>Overall_grade</th>\n",
       "      <th>pass_math</th>\n",
       "      <th>pass_reading</th>\n",
       "      <th>pass_writing</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>72</td>\n",
       "      <td>72</td>\n",
       "      <td>74</td>\n",
       "      <td>218</td>\n",
       "      <td>72.666667</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>69</td>\n",
       "      <td>90</td>\n",
       "      <td>88</td>\n",
       "      <td>247</td>\n",
       "      <td>82.333333</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>B</td>\n",
       "      <td>B</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>90</td>\n",
       "      <td>95</td>\n",
       "      <td>93</td>\n",
       "      <td>278</td>\n",
       "      <td>92.666667</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>A</td>\n",
       "      <td>A</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>47</td>\n",
       "      <td>57</td>\n",
       "      <td>44</td>\n",
       "      <td>148</td>\n",
       "      <td>49.333333</td>\n",
       "      <td>6</td>\n",
       "      <td>5</td>\n",
       "      <td>F</td>\n",
       "      <td>F</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>76</td>\n",
       "      <td>78</td>\n",
       "      <td>75</td>\n",
       "      <td>229</td>\n",
       "      <td>76.333333</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   gender  race/ethnicity      ...       pass_reading  pass_writing\n",
       "0       0               2      ...                  1             1\n",
       "1       0               3      ...                  1             1\n",
       "2       0               2      ...                  1             1\n",
       "3       1               1      ...                  1             1\n",
       "4       1               3      ...                  1             1\n",
       "\n",
       "[5 rows x 17 columns]"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Grade_reading'] = data['Grade_reading'].replace('O',0)\n",
    "data['Grade_reading'] = data['Grade_reading'].replace('A',1)\n",
    "data['Grade_reading'] = data['Grade_reading'].replace('B',2)\n",
    "data['Grade_reading'] = data['Grade_reading'].replace('C',3)\n",
    "data['Grade_reading'] = data['Grade_reading'].replace('D',4)\n",
    "data['Grade_reading'] = data['Grade_reading'].replace('E',5)\n",
    "data['Grade_reading'] = data['Grade_reading'].replace('F',6)\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T21:50:57.357221Z",
     "iopub.status.busy": "2022-01-05T21:50:57.356874Z",
     "iopub.status.idle": "2022-01-05T21:50:57.404834Z",
     "shell.execute_reply": "2022-01-05T21:50:57.404154Z",
     "shell.execute_reply.started": "2022-01-05T21:50:57.357161Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>race/ethnicity</th>\n",
       "      <th>parental level of education</th>\n",
       "      <th>lunch</th>\n",
       "      <th>test preparation course</th>\n",
       "      <th>math score</th>\n",
       "      <th>reading score</th>\n",
       "      <th>writing score</th>\n",
       "      <th>Total marks</th>\n",
       "      <th>Percentage</th>\n",
       "      <th>Grade_math</th>\n",
       "      <th>Grade_reading</th>\n",
       "      <th>Grade_writing</th>\n",
       "      <th>Overall_grade</th>\n",
       "      <th>pass_math</th>\n",
       "      <th>pass_reading</th>\n",
       "      <th>pass_writing</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>72</td>\n",
       "      <td>72</td>\n",
       "      <td>74</td>\n",
       "      <td>218</td>\n",
       "      <td>72.666667</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>C</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>69</td>\n",
       "      <td>90</td>\n",
       "      <td>88</td>\n",
       "      <td>247</td>\n",
       "      <td>82.333333</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>B</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>90</td>\n",
       "      <td>95</td>\n",
       "      <td>93</td>\n",
       "      <td>278</td>\n",
       "      <td>92.666667</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>A</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>47</td>\n",
       "      <td>57</td>\n",
       "      <td>44</td>\n",
       "      <td>148</td>\n",
       "      <td>49.333333</td>\n",
       "      <td>6</td>\n",
       "      <td>5</td>\n",
       "      <td>6</td>\n",
       "      <td>F</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>76</td>\n",
       "      <td>78</td>\n",
       "      <td>75</td>\n",
       "      <td>229</td>\n",
       "      <td>76.333333</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>C</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   gender  race/ethnicity      ...       pass_reading  pass_writing\n",
       "0       0               2      ...                  1             1\n",
       "1       0               3      ...                  1             1\n",
       "2       0               2      ...                  1             1\n",
       "3       1               1      ...                  1             1\n",
       "4       1               3      ...                  1             1\n",
       "\n",
       "[5 rows x 17 columns]"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Grade_writing'] = data['Grade_writing'].replace('O',0)\n",
    "data['Grade_writing'] = data['Grade_writing'].replace('A',1)\n",
    "data['Grade_writing'] = data['Grade_writing'].replace('B',2)\n",
    "data['Grade_writing'] = data['Grade_writing'].replace('C',3)\n",
    "data['Grade_writing'] = data['Grade_writing'].replace('D',4)\n",
    "data['Grade_writing'] = data['Grade_writing'].replace('E',5)\n",
    "data['Grade_writing'] = data['Grade_writing'].replace('F',6)\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T21:50:59.529060Z",
     "iopub.status.busy": "2022-01-05T21:50:59.528771Z",
     "iopub.status.idle": "2022-01-05T21:50:59.577522Z",
     "shell.execute_reply": "2022-01-05T21:50:59.576435Z",
     "shell.execute_reply.started": "2022-01-05T21:50:59.529024Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>race/ethnicity</th>\n",
       "      <th>parental level of education</th>\n",
       "      <th>lunch</th>\n",
       "      <th>test preparation course</th>\n",
       "      <th>math score</th>\n",
       "      <th>reading score</th>\n",
       "      <th>writing score</th>\n",
       "      <th>Total marks</th>\n",
       "      <th>Percentage</th>\n",
       "      <th>Grade_math</th>\n",
       "      <th>Grade_reading</th>\n",
       "      <th>Grade_writing</th>\n",
       "      <th>Overall_grade</th>\n",
       "      <th>pass_math</th>\n",
       "      <th>pass_reading</th>\n",
       "      <th>pass_writing</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>72</td>\n",
       "      <td>72</td>\n",
       "      <td>74</td>\n",
       "      <td>218</td>\n",
       "      <td>72.666667</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>69</td>\n",
       "      <td>90</td>\n",
       "      <td>88</td>\n",
       "      <td>247</td>\n",
       "      <td>82.333333</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>90</td>\n",
       "      <td>95</td>\n",
       "      <td>93</td>\n",
       "      <td>278</td>\n",
       "      <td>92.666667</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>47</td>\n",
       "      <td>57</td>\n",
       "      <td>44</td>\n",
       "      <td>148</td>\n",
       "      <td>49.333333</td>\n",
       "      <td>6</td>\n",
       "      <td>5</td>\n",
       "      <td>6</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>76</td>\n",
       "      <td>78</td>\n",
       "      <td>75</td>\n",
       "      <td>229</td>\n",
       "      <td>76.333333</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   gender  race/ethnicity      ...       pass_reading  pass_writing\n",
       "0       0               2      ...                  1             1\n",
       "1       0               3      ...                  1             1\n",
       "2       0               2      ...                  1             1\n",
       "3       1               1      ...                  1             1\n",
       "4       1               3      ...                  1             1\n",
       "\n",
       "[5 rows x 17 columns]"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Overall_grade'] = data['Overall_grade'].replace('O',0)\n",
    "data['Overall_grade'] = data['Overall_grade'].replace('A',1)\n",
    "data['Overall_grade'] = data['Overall_grade'].replace('B',2)\n",
    "data['Overall_grade'] = data['Overall_grade'].replace('C',3)\n",
    "data['Overall_grade'] = data['Overall_grade'].replace('D',4)\n",
    "data['Overall_grade'] = data['Overall_grade'].replace('E',5)\n",
    "data['Overall_grade'] = data['Overall_grade'].replace('F',6)\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T21:51:02.572340Z",
     "iopub.status.busy": "2022-01-05T21:51:02.572023Z",
     "iopub.status.idle": "2022-01-05T21:51:02.580458Z",
     "shell.execute_reply": "2022-01-05T21:51:02.579361Z",
     "shell.execute_reply.started": "2022-01-05T21:51:02.572287Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1000, 14)\n",
      "(1000,)\n"
     ]
    }
   ],
   "source": [
    "x= data.iloc[:,:14]\n",
    "y = data.iloc[:,14]\n",
    "print(x.shape)\n",
    "print(y.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T22:17:07.057885Z",
     "iopub.status.busy": "2022-01-05T22:17:07.057479Z",
     "iopub.status.idle": "2022-01-05T22:17:07.069676Z",
     "shell.execute_reply": "2022-01-05T22:17:07.068120Z",
     "shell.execute_reply.started": "2022-01-05T22:17:07.057823Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(800, 14)\n",
      "(200, 14)\n",
      "(800,)\n",
      "(200,)\n"
     ]
    }
   ],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 0)\n",
    "print(x_train.shape)\n",
    "print(x_test.shape)\n",
    "print(y_train.shape)\n",
    "print(y_test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T22:17:55.890198Z",
     "iopub.status.busy": "2022-01-05T22:17:55.889861Z",
     "iopub.status.idle": "2022-01-05T22:17:55.904090Z",
     "shell.execute_reply": "2022-01-05T22:17:55.902993Z",
     "shell.execute_reply.started": "2022-01-05T22:17:55.890145Z"
    }
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/conda/lib/python3.6/site-packages/sklearn/preprocessing/data.py:625: DataConversionWarning: Data with input dtype int64, float64 were all converted to float64 by StandardScaler.\n",
      "  return self.partial_fit(X, y)\n",
      "/opt/conda/lib/python3.6/site-packages/sklearn/base.py:462: DataConversionWarning: Data with input dtype int64, float64 were all converted to float64 by StandardScaler.\n",
      "  return self.fit(X, **fit_params).transform(X)\n",
      "/opt/conda/lib/python3.6/site-packages/ipykernel_launcher.py:4: DataConversionWarning: Data with input dtype int64, float64 were all converted to float64 by StandardScaler.\n",
      "  after removing the cwd from sys.path.\n"
     ]
    }
   ],
   "source": [
    "from sklearn.preprocessing import StandardScaler\n",
    "sc = StandardScaler()\n",
    "x_train = sc.fit_transform(x_train)\n",
    "x_test = sc.transform(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T22:18:11.028832Z",
     "iopub.status.busy": "2022-01-05T22:18:11.028501Z",
     "iopub.status.idle": "2022-01-05T22:18:11.041833Z",
     "shell.execute_reply": "2022-01-05T22:18:11.040310Z",
     "shell.execute_reply.started": "2022-01-05T22:18:11.028791Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "GaussianNB(priors=None, var_smoothing=1e-09)"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.naive_bayes import GaussianNB\n",
    "classifier = GaussianNB()\n",
    "classifier.fit(x_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T22:18:26.606334Z",
     "iopub.status.busy": "2022-01-05T22:18:26.606019Z",
     "iopub.status.idle": "2022-01-05T22:18:26.612176Z",
     "shell.execute_reply": "2022-01-05T22:18:26.611125Z",
     "shell.execute_reply.started": "2022-01-05T22:18:26.606293Z"
    }
   },
   "outputs": [],
   "source": [
    "y_pred  =  classifier.predict(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T22:19:13.658399Z",
     "iopub.status.busy": "2022-01-05T22:19:13.658015Z",
     "iopub.status.idle": "2022-01-05T22:19:13.666359Z",
     "shell.execute_reply": "2022-01-05T22:19:13.665219Z",
     "shell.execute_reply.started": "2022-01-05T22:19:13.658339Z"
    }
   },
   "outputs": [],
   "source": [
    "from sklearn.metrics import confusion_matrix,accuracy_score\n",
    "cm = confusion_matrix(y_test, y_pred)\n",
    "ac = accuracy_score(y_test,y_pred)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T22:25:27.132693Z",
     "iopub.status.busy": "2022-01-05T22:25:27.131757Z",
     "iopub.status.idle": "2022-01-05T22:25:27.213391Z",
     "shell.execute_reply": "2022-01-05T22:25:27.212464Z",
     "shell.execute_reply.started": "2022-01-05T22:25:27.132621Z"
    }
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/conda/lib/python3.6/site-packages/sklearn/linear_model/logistic.py:433: FutureWarning: Default solver will be changed to 'lbfgs' in 0.22. Specify a solver to silence this warning.\n",
      "  FutureWarning)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "98.88"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Logistic Regression\n",
    "\n",
    "logreg = LogisticRegression()\n",
    "logreg.fit(x_train, y_train)\n",
    "x_pred = logreg.predict(x_test)\n",
    "acc_log = round(logreg.score(x_train, y_train) * 100, 2)\n",
    "acc_log"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T22:25:58.902025Z",
     "iopub.status.busy": "2022-01-05T22:25:58.901718Z",
     "iopub.status.idle": "2022-01-05T22:25:58.907590Z",
     "shell.execute_reply": "2022-01-05T22:25:58.906741Z",
     "shell.execute_reply.started": "2022-01-05T22:25:58.901988Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['gender' 'race/ethnicity' 'parental level of education' 'lunch'\n",
      " 'test preparation course' 'math score' 'reading score' 'writing score'\n",
      " 'Total marks' 'Percentage' 'Grade_math' 'Grade_reading' 'Grade_writing'\n",
      " 'Overall_grade' 'pass_math' 'pass_reading' 'pass_writing']\n"
     ]
    }
   ],
   "source": [
    "print(data.columns.values)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T22:26:17.969425Z",
     "iopub.status.busy": "2022-01-05T22:26:17.969088Z",
     "iopub.status.idle": "2022-01-05T22:26:18.005554Z",
     "shell.execute_reply": "2022-01-05T22:26:18.004654Z",
     "shell.execute_reply.started": "2022-01-05T22:26:17.969375Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>race/ethnicity</th>\n",
       "      <th>parental level of education</th>\n",
       "      <th>lunch</th>\n",
       "      <th>test preparation course</th>\n",
       "      <th>math score</th>\n",
       "      <th>reading score</th>\n",
       "      <th>writing score</th>\n",
       "      <th>Total marks</th>\n",
       "      <th>Percentage</th>\n",
       "      <th>Grade_math</th>\n",
       "      <th>Grade_reading</th>\n",
       "      <th>Grade_writing</th>\n",
       "      <th>Overall_grade</th>\n",
       "      <th>pass_math</th>\n",
       "      <th>pass_reading</th>\n",
       "      <th>pass_writing</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>72</td>\n",
       "      <td>72</td>\n",
       "      <td>74</td>\n",
       "      <td>218</td>\n",
       "      <td>72.666667</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>69</td>\n",
       "      <td>90</td>\n",
       "      <td>88</td>\n",
       "      <td>247</td>\n",
       "      <td>82.333333</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>90</td>\n",
       "      <td>95</td>\n",
       "      <td>93</td>\n",
       "      <td>278</td>\n",
       "      <td>92.666667</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>47</td>\n",
       "      <td>57</td>\n",
       "      <td>44</td>\n",
       "      <td>148</td>\n",
       "      <td>49.333333</td>\n",
       "      <td>6</td>\n",
       "      <td>5</td>\n",
       "      <td>6</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>76</td>\n",
       "      <td>78</td>\n",
       "      <td>75</td>\n",
       "      <td>229</td>\n",
       "      <td>76.333333</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   gender  race/ethnicity      ...       pass_reading  pass_writing\n",
       "0       0               2      ...                  1             1\n",
       "1       0               3      ...                  1             1\n",
       "2       0               2      ...                  1             1\n",
       "3       1               1      ...                  1             1\n",
       "4       1               3      ...                  1             1\n",
       "\n",
       "[5 rows x 17 columns]"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T22:26:36.147830Z",
     "iopub.status.busy": "2022-01-05T22:26:36.147398Z",
     "iopub.status.idle": "2022-01-05T22:26:36.181261Z",
     "shell.execute_reply": "2022-01-05T22:26:36.180530Z",
     "shell.execute_reply.started": "2022-01-05T22:26:36.147791Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>race/ethnicity</th>\n",
       "      <th>parental level of education</th>\n",
       "      <th>lunch</th>\n",
       "      <th>test preparation course</th>\n",
       "      <th>math score</th>\n",
       "      <th>reading score</th>\n",
       "      <th>writing score</th>\n",
       "      <th>Total marks</th>\n",
       "      <th>Percentage</th>\n",
       "      <th>Grade_math</th>\n",
       "      <th>Grade_reading</th>\n",
       "      <th>Grade_writing</th>\n",
       "      <th>Overall_grade</th>\n",
       "      <th>pass_math</th>\n",
       "      <th>pass_reading</th>\n",
       "      <th>pass_writing</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>995</th>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>88</td>\n",
       "      <td>99</td>\n",
       "      <td>95</td>\n",
       "      <td>282</td>\n",
       "      <td>94.000000</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>996</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>62</td>\n",
       "      <td>55</td>\n",
       "      <td>55</td>\n",
       "      <td>172</td>\n",
       "      <td>57.333333</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>997</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>59</td>\n",
       "      <td>71</td>\n",
       "      <td>65</td>\n",
       "      <td>195</td>\n",
       "      <td>65.000000</td>\n",
       "      <td>5</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>998</th>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>68</td>\n",
       "      <td>78</td>\n",
       "      <td>77</td>\n",
       "      <td>223</td>\n",
       "      <td>74.333333</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>999</th>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>77</td>\n",
       "      <td>86</td>\n",
       "      <td>86</td>\n",
       "      <td>249</td>\n",
       "      <td>83.000000</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     gender  race/ethnicity      ...       pass_reading  pass_writing\n",
       "995       0               5      ...                  1             1\n",
       "996       1               3      ...                  1             1\n",
       "997       0               3      ...                  1             1\n",
       "998       0               4      ...                  1             1\n",
       "999       0               4      ...                  1             1\n",
       "\n",
       "[5 rows x 17 columns]"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T22:29:14.362164Z",
     "iopub.status.busy": "2022-01-05T22:29:14.361701Z",
     "iopub.status.idle": "2022-01-05T22:29:14.379846Z",
     "shell.execute_reply": "2022-01-05T22:29:14.379206Z",
     "shell.execute_reply.started": "2022-01-05T22:29:14.362123Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "98.88"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Support Vector Machines\n",
    "\n",
    "svc = SVC()\n",
    "svc.fit(x_train, y_train)\n",
    "y_pred = svc.predict(x_test)\n",
    "acc_svc = round(svc.score(x_train, y_train) * 100, 2)\n",
    "acc_svc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T22:30:33.021543Z",
     "iopub.status.busy": "2022-01-05T22:30:33.021078Z",
     "iopub.status.idle": "2022-01-05T22:30:33.043131Z",
     "shell.execute_reply": "2022-01-05T22:30:33.042408Z",
     "shell.execute_reply.started": "2022-01-05T22:30:33.021500Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "98.62"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "knn = KNeighborsClassifier(n_neighbors = 3)\n",
    "knn.fit(x_train, y_train)\n",
    "y_pred = knn.predict(x_test)\n",
    "acc_knn = round(knn.score(x_train, y_train) * 100, 2)\n",
    "acc_knn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T22:31:09.940584Z",
     "iopub.status.busy": "2022-01-05T22:31:09.940235Z",
     "iopub.status.idle": "2022-01-05T22:31:09.950987Z",
     "shell.execute_reply": "2022-01-05T22:31:09.949996Z",
     "shell.execute_reply.started": "2022-01-05T22:31:09.940517Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "91.62"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Gaussian Naive Bayes\n",
    "\n",
    "gaussian = GaussianNB()\n",
    "gaussian.fit(x_train, y_train)\n",
    "y_pred = gaussian.predict(x_test)\n",
    "acc_gaussian = round(gaussian.score(x_train, y_train) * 100, 2)\n",
    "acc_gaussian"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T22:31:50.016797Z",
     "iopub.status.busy": "2022-01-05T22:31:50.016125Z",
     "iopub.status.idle": "2022-01-05T22:31:50.027454Z",
     "shell.execute_reply": "2022-01-05T22:31:50.026058Z",
     "shell.execute_reply.started": "2022-01-05T22:31:50.016747Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100.0"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Decision Tree\n",
    "\n",
    "decision_tree = DecisionTreeClassifier()\n",
    "decision_tree.fit(x_train, y_train)\n",
    "y_pred = decision_tree.predict(x_test)\n",
    "acc_decision_tree = round(decision_tree.score(x_train, y_train) * 100, 2)\n",
    "acc_decision_tree"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T22:32:30.118068Z",
     "iopub.status.busy": "2022-01-05T22:32:30.117665Z",
     "iopub.status.idle": "2022-01-05T22:32:30.263600Z",
     "shell.execute_reply": "2022-01-05T22:32:30.262442Z",
     "shell.execute_reply.started": "2022-01-05T22:32:30.117996Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100.0"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "random_forest = RandomForestClassifier(n_estimators=100)\n",
    "random_forest.fit(x_train, y_train)\n",
    "y_pred = random_forest.predict(x_test)\n",
    "random_forest.score(x_train, y_train)\n",
    "acc_random_forest = round(random_forest.score(x_train, y_train) * 100, 2)\n",
    "acc_random_forest"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T22:35:27.374961Z",
     "iopub.status.busy": "2022-01-05T22:35:27.374637Z",
     "iopub.status.idle": "2022-01-05T22:35:27.395393Z",
     "shell.execute_reply": "2022-01-05T22:35:27.394462Z",
     "shell.execute_reply.started": "2022-01-05T22:35:27.374923Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>Score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Random Forest</td>\n",
       "      <td>100.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Decision Tree</td>\n",
       "      <td>100.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Support Vector Machines</td>\n",
       "      <td>98.88</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Logistic Regression</td>\n",
       "      <td>98.88</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>KNN</td>\n",
       "      <td>98.62</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Naive Bayes</td>\n",
       "      <td>91.62</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                     Model   Score\n",
       "3            Random Forest  100.00\n",
       "5            Decision Tree  100.00\n",
       "0  Support Vector Machines   98.88\n",
       "2      Logistic Regression   98.88\n",
       "1                      KNN   98.62\n",
       "4              Naive Bayes   91.62"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "models = pd.DataFrame({\n",
    "    'Model': ['Support Vector Machines', 'KNN', 'Logistic Regression', \n",
    "              'Random Forest', 'Naive Bayes', \n",
    "              'Decision Tree'],\n",
    "    'Score': [acc_svc, acc_knn, acc_log, \n",
    "              acc_random_forest,acc_gaussian,\n",
    "               acc_decision_tree]})\n",
    "models.sort_values(by='Score', ascending=False)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
