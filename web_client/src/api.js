import request from 'superagent';

const FINNEGAN_FOREVER_URL = 'https://drsvfxtdvi.execute-api.us-east-1.amazonaws.com/dev/passage';

/**
 *  Fetch from the finnegan_forever API the current text passage and the seconds after which new
 *  passages are read.
 */
export default async function readFinneganPassage () {
    const response = await request.get(FINNEGAN_FOREVER_URL);
    return {text: response.body.passage, readingEvery: response.body.reading_every};
}
