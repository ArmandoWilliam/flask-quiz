from flask import Flask, jsonify, request, render_template, session, redirect, url_for
from flask_session import Session

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


quiz_data = {
    'title': 'Quiz su Intelligenza Artificiale e Python',
    'questions': [
        {
            'id': 1,
            'question_text': 'Quale libreria Python è ampiamente utilizzata per lo sviluppo di reti neurali?',
            'options': ['TensorFlow', 'Pandas', 'Matplotlib', 'BeautifulSoup'],
            'correct_answer': 'TensorFlow'
        },
        {
            'id': 2,
            'question_text': 'Quale algoritmo è comunemente usato per il riconoscimento facciale nella visione computerizzata?',
            'options': ['K-Means', 'Random Forest', 'Convolutional Neural Networks', 'Linear Regression'],
            'correct_answer': 'Convolutional Neural Networks'
        },
        {
            'id': 3,
            'question_text': 'Quale libreria Python è spesso utilizzata per il Natural Language Processing?',
            'options': ['NumPy', 'NLTK', 'Scikit-learn', 'Matplotlib'],
            'correct_answer': 'NLTK'
        },
        {
            'id': 4,
            'question_text': 'Quale tecnica di apprendimento automatico è utilizzata per generare testo simile a quello umano?',
            'options': ['Clustering', 'Regressione logistica', 'Reti neurali ricorrenti', 'Support Vector Machines'],
            'correct_answer': 'Reti neurali ricorrenti'
        },
        {
            'id': 5,
            'question_text': 'Quale framework Python è comunemente usato per lo sviluppo di applicazioni web con integrazione di AI?',
            'options': ['Django', 'Flask', 'FastAPI', 'Pyramid'],
            'correct_answer': 'Flask'
        },
        {
            'id': 6,
            'question_text': 'Quale tecnica di visione computerizzata è utilizzata per rilevare i bordi in un\'immagine?',
            'options': ['Thresholding', 'Rilevamento di Canny', 'Segmentazione', 'Trasformata di Hough'],
            'correct_answer': 'Rilevamento di Canny'
        },
        {
            'id': 7,
            'question_text': 'Quale metodo di NLP è utilizzato per determinare il sentimento di un testo?',
            'options': ['Tokenizzazione', 'Analisi del sentimento', 'Part-of-speech tagging', 'Named Entity Recognition'],
            'correct_answer': 'Analisi del sentimento'
        },
        {
            'id': 8,
            'question_text': 'Quale libreria Python è comunemente usata per la manipolazione e l\'analisi dei dati nell\'AI?',
            'options': ['Pandas', 'Requests', 'Beautiful Soup', 'PyQt'],
            'correct_answer': 'Pandas'
        },
        {
            'id': 9,
            'question_text': 'Quale tipo di rete neurale è particolarmente efficace per l\'elaborazione di sequenze temporali?',
            'options': ['Feedforward Neural Network', 'Convolutional Neural Network', 'Recurrent Neural Network', 'Generative Adversarial Network'],
            'correct_answer': 'Recurrent Neural Network'
        },
        {
            'id': 10,
            'question_text': 'Quale tecnica di AI è utilizzata per ottimizzare i parametri di un modello di apprendimento automatico?',
            'options': ['Gradient Descent', 'K-Nearest Neighbors', 'Decision Trees', 'Naive Bayes'],
            'correct_answer': 'Gradient Descent'
        },
    ]
}

@app.route('/', methods=['GET'])
def show_quiz():
    if 'best_score' not in session:
        session['best_score'] = 0

    return render_template('quiz_template.html',
                           title=quiz_data['title'],
                           quiz_title=quiz_data['title'],
                           questions=quiz_data['questions'],
                           best_score=round(session['best_score'], 2))

@app.route('/submit', methods=['POST'])
def submit_quiz():
    user_answers = {key: value for key, value in request.form.items()}
    score, total_questions = calculate_score(user_answers)
    percentage_score = (score / total_questions) * 100

    if percentage_score > session['best_score']:
        session['best_score'] = percentage_score

    return render_template('quiz_template.html',
                           title=quiz_data['title'],
                           quiz_title=quiz_data['title'],
                           questions=quiz_data['questions'],
                           score=score,
                           total_questions=total_questions,
                           best_score=round(session['best_score'], 2))

def calculate_score(user_answers):
    score = 0
    total_questions = len(quiz_data['questions'])

    for question in quiz_data['questions']:
        question_id = question['id']
        user_answer = user_answers.get(str(question_id))
        if user_answer and user_answer == question['correct_answer']:
            score += 1
    return score, total_questions

@app.route('/reset_best_score', methods=['POST'])
def reset_best_score():
    print('Punteggio migliore prima del reset:', session.get('best_score', 'Non impostato'))
    session['best_score'] = 0
    print('Punteggio migliore dopo il reset:', session['best_score'])
    return redirect(url_for('show_quiz')) 

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3000)