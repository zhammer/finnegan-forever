import request from 'superagent';

const FINNEGAN_FOREVER_URL = 'https://drsvfxtdvi.execute-api.us-east-1.amazonaws.com/dev/passage';

export default async function readFinneganPassage () {
    const response = await request.get(FINNEGAN_FOREVER_URL);
    return {text: response.body.passage, readingEvery: response.body.reading_every};
}
