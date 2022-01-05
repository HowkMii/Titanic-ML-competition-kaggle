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
     "iopub.execute_input": "2022-01-05T20:08:36.155628Z",
     "iopub.status.busy": "2022-01-05T20:08:36.155120Z",
     "iopub.status.idle": "2022-01-05T20:08:36.166202Z",
     "shell.execute_reply": "2022-01-05T20:08:36.164941Z",
     "shell.execute_reply.started": "2022-01-05T20:08:36.155581Z"
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
    "%matplotlib inline"
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
       "B    135\n",
       "F    135\n",
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
     "iopub.execute_input": "2022-01-05T20:24:15.527250Z",
     "iopub.status.busy": "2022-01-05T20:24:15.526582Z",
     "iopub.status.idle": "2022-01-05T20:24:16.459468Z",
     "shell.execute_reply": "2022-01-05T20:24:16.458390Z",
     "shell.execute_reply.started": "2022-01-05T20:24:15.527194Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x7f9b1563b9e8>"
      ]
     },
     "execution_count": 12,
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
    "sns.countplot(x = \"reading score\", data = data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
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
     "execution_count": 13,
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
   "execution_count": 14,
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
   "execution_count": 15,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-01-05T20:26:34.424716Z",
     "iopub.status.busy": "2022-01-05T20:26:34.423979Z",
     "iopub.status.idle": "2022-01-05T20:26:34.656481Z",
     "shell.execute_reply": "2022-01-05T20:26:34.655442Z",
     "shell.execute_reply.started": "2022-01-05T20:26:34.424662Z"
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
    "sns.countplot(x = \"Grade_writing\", data = data, order = order_grade, palette = \"GnBu_d\")\n",
    "_ = plt.xlabel(\"Grades in writing\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
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
     "execution_count": 16,
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
   "execution_count": 17,
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
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": []
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
