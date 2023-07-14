# LP/CP Programming Contest 2023

The traditional [LP/CP Programming Contest](https://lpcp-contest.github.io/) will be run **on site** during ICLP 2023.
It will be a two hours session, taking place on Thursday, 13 July, from 16:30 to 18:30.
The LP/CP Programming Contest 2023 will be held in person, with each team consisting of up to three participants, and is hosted at the ICLP 2023 conference venue, the Imperial College London.

**Results, stats and winner** will be announced shortly after the contest at the ICLP 2023 conference banquet.

The contest combines some features of Prolog programming contest, Answer Set Programming (ASP) Model and Solve contest, and Constraint Programming (CP) Model and Solve contest.
A variety of systems can be used in the competition, and as in the previous edition participants are not constrained to use a single system and can also combine declarative and imperative programming languages.
Submitted solutions are expected to have a declarative predominant core.

Input and output format of problems will be provided according to some easy-to-parse representation, and similarly output must be provided according to some easy-to-write format.
(Please, have a look at the [previous edition](https://github.com/alviano/lpcp-contest-2022) of the contest to get an idea of the input and output format.)


## Systems

Any declarative problem solving language or system can be used.
In particular, a Docker image where the systems

* Ciao Prolog: http://ciao-lang.org
* ECLiPSe Prolog: http://eclipseclp.org
* GNU Prolog: http://gprolog.org
* SWI-Prolog: http://www.swi-prolog.org
* XSB Prolog: http://xsb.sourceforge.net
* IDP: https://dtai.cs.kuleuven.be/pages/software/idp
* MiniZinc: http://www.minizinc.org
* Picat: http://picat-lang.org
* Potassco: https://potassco.org

are installed is available from the 2019 edition of the contest.
Details on the installation and usage of the Docker image can be found [here](https://github.com/lpcp-contest/docker-lpcpsys).

However, usage of the Docker image is optional, and other systems can be run as well. When needed, we will ask for some help to run your solutions.


## Scoring

Participants will be ranked by **number of solved instances**.
A solution is valid as soon as it does not produce wrong answers for the tested instances.

In case of an **optimization problem**, the best solution(s) for an instance provided by some participant will be awarded a point. Correct yet suboptimal answers are not considered wrong but won't receive points for the problem instance under consideration.

Ties are broken by time of the last submissions contributing some points.
Further ties are broken by cumulative execution time.

Participants will receive feedback on the number of solved instances and on errors of their submissions.
As a general suggestion, **submit solutions as soon as you have them**.


## Registration

Send an email to lpcp2023@easychair.org with subject **LP/CP Programming Contest 2023 - Registration** and the following content:

* Team name;
* List of up to three participants and their affiliations;
* One or more email addresses to receive feedback.

And of course: Join us for the LP/CP Programming Contest 2023 session on **Thursday, 13 July, from 16:30 to 18:30!**


## Submission

Via [EasyChair](https://easychair.org/conferences/?conf=iclp2023).
Select the **Competition** track for the submission of solutions.

For each problem you solve, submit a ZIP archive with all files needed to run your solution.
The title must obey the following format:

```
team-name:problem-number:version
```

A good entry-point is a script like `run.sh` reading input instances from STDIN and producing output on STDOUT (see [problem-0](problem-0/example-solution-using-asp)).
If you opt for a different entry-point or different usage, provide instructions on how to execute your solution in the abstract.
We may ask support to run your solution at the end of the contest.

Keywords are not important, but you have to provide at least three of them. Use the following:

```
one
two
three
```

Please make sure that you have an EasyChair account for being ready to submit.


## Checkers

The Python client to invoke the remote checkers expects two command-line parameters, namely the problem-ID and the instance-ID.
The solution to be checked is read from standard input.
Before the contest, the checker is restricted to an example problem.
It will be replaced to the unrestricted version during the contest.

Let us consider [problem-0](problem-0) (taken from a previous edition), and its first instance (i.e., instance-1).
If the solution to be checked is stored in file `instance.1.out`, the checker can be run with one of the following command-lines:
```bash
$ ./checker.py 0 1 <instance.1.out
$ ./checker.py 0 1 <instance.1.out --no-browser
```

Errors are printed in the standard output.
The first command-line also opens an ASP Chef visualization of the solution, as well as of errors (if any).

Note also that folder [problem-0](problem-0) includes an example solution using ASP.
Input is parsed with a generic Python script, which can be easily adapted to other systems.
Similarly, the output of the ASP engine is mapped to CSV by another Python script.
The entry point to execute the ASP solution is the bash script `run.sh`.


## Participants

In alphabetical order:
- **aaunical**: Wolfgang Faber (University of Klagenfurt, Austria), Giuseppe Mazzotta (University of Calabria, Italy), Alice Tarzariol (University of Klagenfurt, Austria)
- **ASP lovers**: Carmine Dodaro (University of Calabria, Italy), Alessandro Quarta (University of Calabria and Sapienza University, Italy), Francesco Ricca (University of Calabria, Italy)
- **NotYet**: Matti Berthold (Universität Leipzig, Germany), Richard Comploi-Taupe (Siemens, Austria)
- **SpaghettiLP**: Damiano Azzolini (University of Ferrara, Italy), Stefano Forti (University of Pisa, Italy), Antonio Ielo (University of Calabria, Italy)

### 🏆 Winner: SpaghettiLP

Members:
- Damiano Azzolini (University of Ferrara, Italy)
- Stefano Forti (University of Pisa, Italy)
- Antonio Ielo (University of Calabria, Italy)

Stats:
- Points: 10/25
- Time of last scored point: 1h20
- Systems: clingo (problem-1), SWI-prolog (problem-4)


### 🥈 Runner Up: aaunical

Members:
- Wolfgang Faber (University of Klagenfurt, Austria)
- Giuseppe Mazzotta (University of Calabria, Italy)
- Alice Tarzariol (University of Klagenfurt, Austria)

Stats:
- Points: 10/25
- Time of last scored point: 1h50 minutes
- System: ASP Chef (problem-1, problem-3)


### 🥉 Podium Finish: NotYet

Members:
- Matti Berthold (Universität Leipzig, Germany)
- Richard Comploi-Taupe (Siemens, Austria)

Stats:
- Points: 10/25
- Time of last scored point: 1h54
- System: clingo (problem-1, problem-4)


## Organization

- [Mario Alviano](https://alviano.net)
- [Martin Gebser](https://ainf.aau.at/prosys)
