import request from 'superagent';

export default async function readPassage (finneganForeverUrl) {
    const response = await request.get(finneganForeverUrl);
    return response.body;
}
